import json
import platform
import shutil
import subprocess
import os
from datetime import datetime


def detect_mode():
    """
    Decide how this agent should run
    """
    if platform.system() == "Linux":
        if shutil.which("nvidia-smi"):
            return "GPU_REAL"
        return "NO_GPU"
    return "UNSUPPORTED"


def get_system_metrics():
    """
    Collect basic system metrics (Linux-safe)
    """
    load1, load5, load15 = os.getloadavg()
    return {
        "load_avg_1m": round(load1, 2),
        "load_avg_5m": round(load5, 2),
        "load_avg_15m": round(load15, 2)
    }


def get_gpu_metrics():
    """
    Collect GPU metrics using nvidia-smi
    Runs ONLY when GPU is present
    """
    try:
        cmd = [
            "nvidia-smi",
            "--query-gpu=index,utilization.gpu,memory.used,memory.total,temperature.gpu",
            "--format=csv,noheader,nounits"
        ]
        output = subprocess.check_output(cmd).decode().strip().split("\n")

        gpus = []
        for line in output:
            index, util, mem_used, mem_total, temp = line.split(", ")
            gpus.append({
                "gpu_id": int(index),
                "utilization_percent": int(util),
                "memory_used_mb": int(mem_used),
                "memory_total_mb": int(mem_total),
                "temperature_c": int(temp)
            })
        return gpus

    except Exception as e:
        return {"error": str(e)}


def main():
    mode = detect_mode()

    data = {
        "project": "InfraMind GPU Agent",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "os": platform.system(),
        "mode": mode,
        "system": get_system_metrics(),
        "status": "RUNNING"
    }

    if mode == "GPU_REAL":
        data["gpus"] = get_gpu_metrics()

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

