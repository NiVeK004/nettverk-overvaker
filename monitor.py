# hei :)
from ping3 import ping
import time

def check_device(ip):
    response = ping(ip, timeout=1)
    if response is not None:
        return {"ip": ip, "status": "Online", "latency": round(response * 1000, 2)}
    else:
        return {"ip": ip, "status": "Offline", "latency": None}

def load_devices(file_path="devices.json"):
    import json
    with open(file_path, "r") as f:
        return json.load(f)

def check_all_devices():
    devices = load_devices()
    results = []
    for ip in devices:
        result = check_device(ip)
        results.append(result)
    return results
