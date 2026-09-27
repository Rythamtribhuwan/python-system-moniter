from flask import Flask, render_template
import psutil
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    hostname = socket.gethostname()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        cpu=cpu,
        ram=ram,
        disk=disk,
        hostname=hostname,
        time=time
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
