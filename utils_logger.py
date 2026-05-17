import csv, os
from datetime import datetime, timezone

def init_logger():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/processing_log.csv"):
        with open("data/processing_log.csv", "w", newline="") as f:
            csv.DictWriter(f, fieldnames=["timestamp", "agent_name", "source_id", "action", "details"]).writeheader()

def log_action(agent_name, source_id, action, details=""):
    init_logger()
    with open("data/processing_log.csv", "a", newline="") as f:
        csv.DictWriter(f, fieldnames=["timestamp", "agent_name", "source_id", "action", "details"]).writerow({
            "timestamp": datetime.now(timezone.utc).isoformat(), "agent_name": agent_name, "source_id": source_id, "action": action, "details": details
        })