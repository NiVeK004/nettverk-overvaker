from flask import Flask, render_template
from monitor import check_all_devices
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    devices = check_all_devices()
    return render_template("index.html", devices=devices)

@app.route("/api/devices")
@app.route("/api/devices")
def api_devices():
    devices = check_all_devices()  # hent enhetdata
    devices_data = [
        {
            "name": f"Enhet {i + 1}",  # kjedelig navn
            "ip": device["ip"],
            "status": device["status"],
            "latency": device["latency"] if device["latency"] is not None else "N/A"
        }
        for i, device in enumerate(devices)
    ]
    return jsonify(devices_data)


if __name__ == "__main__":
    app.run(debug=True)

