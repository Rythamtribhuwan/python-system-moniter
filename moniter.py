import psutil
import time
import socket
import logging
from datetime import datetime

logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("======================================")
print("       PYTHON SYSTEM MONITOR")
print("======================================")

hostname = socket.gethostname()
print("Computer:", hostname)
print("Monitoring started...")

while True:

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    ram_percent = ram.percent
    disk_percent = disk.percent

    print("\n======================================")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("======================================")

    print(f"CPU Usage  : {cpu:.1f}%")
    print(f"RAM Usage  : {ram_percent:.1f}%")
    print(f"Disk Usage : {disk_percent:.1f}%")

    logging.info(
        f"CPU={cpu:.1f}% | RAM={ram_percent:.1f}% | Disk={disk_percent:.1f}%"
    )

    if cpu > 80:
        print("WARNING: CPU usage is above 80%!")
        logging.warning(f"CPU usage is high: {cpu:.1f}%")
        break

    if ram_percent > 80:
        print("WARNING: RAM usage is above 80%!")
        logging.warning(f"RAM usage is high: {ram_percent:.1f}%")
        break

    if disk_percent > 80:
        print("WARNING: Disk usage is above 80%!")
        logging.warning(f"Disk usage is high: {disk_percent:.1f}%")
        break

    print("System Status: Normal")

    time.sleep(2)

print("Monitor stopped.")
