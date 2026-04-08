import pytest
from app.metrics import collect_metrics

def test_metrics_structure():
    data = collect_metrics()

    # Check top-level keys
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data
    assert "system" in data

    # CPU keys
    assert "percent" in data["cpu"]
    assert "cores" in data["cpu"]

    # Memory keys
    for key in ["percent", "total_gb", "used_gb"]:
        assert key in data["memory"]

    # Disk keys
    for key in ["percent", "total_gb", "used_gb", "free_gb"]:
        assert key in data["disk"]

    # System keys
    for key in ["hostname", "platform", "uptime_seconds"]:
        assert key in data["system"]

def test_metrics_values():
    data = collect_metrics()
    assert 0 <= data["cpu"]["percent"] <= 100
    assert data["cpu"]["cores"] > 0
    assert 0 <= data["memory"]["percent"] <= 100
    assert data["memory"]["used_gb"] <= data["memory"]["total_gb"]
    assert 0 <= data["disk"]["percent"] <= 100
    assert data["disk"]["used_gb"] + data["disk"]["free_gb"] <= data["disk"]["total_gb"]
    assert data["system"]["uptime_seconds"] >= 0