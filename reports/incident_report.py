import docker
import time
import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

client = docker.from_env()
TARGETS = ['flask-app']
CHECK_INTERVAL = 5
incidents = []

def get_status(name):
    try:
        return client.containers.get(name).status
    except:
        return "not found"

def generate_report():
    report = {
        "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_incidents": len(incidents),
        "incidents": incidents
    }

    filename = f"/home/osboxes/chaos-lab/reports/incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)

    logger.info(f"📝 Report saved: {filename}")
    print("\n========== INCIDENT REPORT ==========")
    print(f"Generated at : {report['report_generated_at']}")
    print(f"Total Incidents: {report['total_incidents']}")
    for i, inc in enumerate(incidents, 1):
        print(f"\nIncident #{i}")
        print(f"  Container  : {inc['container']}")
        print(f"  Detected   : {inc['detected_at']}")
        print(f"  Recovered  : {inc['recovered_at']}")
        print(f"  Downtime   : {inc['downtime_seconds']} seconds")
    print("=====================================\n")

def monitor():
    logger.info("📋 Incident Reporter Started!")
    prev_status = {t: "running" for t in TARGETS}

    down_since = {}

    try:
        while True:
            for name in TARGETS:
                status = get_status(name)

                if status != "running" and prev_status[name] == "running":
                    down_since[name] = datetime.now()
                    logger.warning(f"🔴 INCIDENT: {name} went DOWN at {down_since[name]}")

                if status == "running" and prev_status[name] != "running":
                    recovered_at = datetime.now()
                    downtime = (recovered_at - down_since[name]).seconds
                    incident = {
                        "container": name,
                        "detected_at": down_since[name].strftime("%Y-%m-%d %H:%M:%S"),
                        "recovered_at": recovered_at.strftime("%Y-%m-%d %H:%M:%S"),
                        "downtime_seconds": downtime
                    }
                    incidents.append(incident)
                    logger.info(f"🟢 RECOVERED: {name} back up! Downtime: {downtime}s")

                prev_status[name] = status
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logger.info("⛔ Stopping reporter, generating final report...")
        generate_report()

if __name__ == '__main__':
    monitor()
