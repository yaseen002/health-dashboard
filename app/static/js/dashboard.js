async function fetchMetrics() {
    try {
        const response = await fetch("/metrics");
        if (!response.ok) throw new Error("Network response was not ok");
        const data = await response.json();

        document.getElementById("cpu").innerText = data.cpu.percent + "%";
        document.getElementById("cpu_cores").innerText = data.cpu.cores;

        document.getElementById("memory").innerText =
            data.memory.percent + "% (" + data.memory.used_gb + " / " + data.memory.total_gb + " GB)";
        document.getElementById("ram_total").innerText = data.memory.total_gb + " GB";

        document.getElementById("disk").innerText =
            data.disk.percent + "% (" + data.disk.used_gb + " / " + data.disk.total_gb + " GB)";
        document.getElementById("disk_free").innerText = data.disk.free_gb + " GB";

        document.getElementById("hostname").innerText = data.system.hostname;
        document.getElementById("platform").innerText = data.system.platform;
        document.getElementById("uptime").innerText = formatUptime(data.system.uptime_seconds);

        // optional: API latency
        const latency = Date.now() - new Date(data.timestamp).getTime();
        document.getElementById("api_latency").innerText = latency + " ms";

    } catch (err) {
        console.error("Failed to fetch metrics:", err);
    }
}

function formatUptime(seconds) {
    const d = Math.floor(seconds / 86400);
    const h = Math.floor((seconds % 86400) / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = Math.floor(seconds % 60);
    return `${d}d ${h}h ${m}m ${s}s`;
}

// fetch every 5 seconds (or your configured refresh interval)
setInterval(fetchMetrics, 5000);
window.onload = fetchMetrics;