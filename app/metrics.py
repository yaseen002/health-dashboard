import psutil
import platform
import socket
import time

def collect_metrics() -> dict:
    """Collect real-time system metrics."""
    # CPU
    cpu_percent = psutil.cpu_percent(interval=0.5)
    cpu_cores = psutil.cpu_count(logical=True)

    # Memory
    mem = psutil.virtual_memory()
    memory_total_gb = round(mem.total / (1024 ** 3), 2)
    memory_used_gb = round(mem.used / (1024 ** 3), 2)
    memory_percent = mem.percent

    # Disk
    disk = psutil.disk_usage("/")
    disk_total_gb = round(disk.total / (1024 ** 3), 2)
    disk_used_gb = round(disk.used / (1024 ** 3), 2)
    disk_free_gb = round(disk.free / (1024 ** 3), 2)
    disk_percent = disk.percent

    # System
    hostname = socket.gethostname()
    system_platform = platform.system() + " " + platform.release()
    uptime_seconds = time.time() - psutil.boot_time()

    return {
        "cpu": {"percent": cpu_percent, "cores": cpu_cores},
        "memory": {
            "percent": memory_percent,
            "total_gb": memory_total_gb,
            "used_gb": memory_used_gb,
        },
        "disk": {
            "percent": disk_percent,
            "total_gb": disk_total_gb,
            "used_gb": disk_used_gb,
            "free_gb": disk_free_gb,
        },
        "system": {
            "hostname": hostname,
            "platform": system_platform,
            "uptime_seconds": int(uptime_seconds),
        },
    }