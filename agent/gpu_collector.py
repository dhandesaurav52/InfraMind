import json
import platform
import shutil
import os
from datetime import datetime

def detect_mode():
    os_name = platform.system()

    if os_name == "Linux":
        if shutil.which("nvidia-smi"):
            return "GPU_REAL"
        else:
            return "NO_GPU"

    return "UNSUPPORTED"

def get_system_metrics():
    load1, load5, load15 = os.getloadavg()
    return {
        "load_avg_1m": load1,
        "load_avg_5m": load5,
        "load_avg_15m": load15
    }

data = {
    "project": "InfraMind GPU Agent",
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "os": platform.system(),
    "mode": detect_mode(),
    "system": get_system_metrics(),
    "status": "RUNNING"
}

print(json.dumps(data, indent=2))

