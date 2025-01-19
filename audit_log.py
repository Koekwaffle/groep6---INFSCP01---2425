import json
from datetime import datetime
import os

AUDIT_LOG_FILE = os.path.join(os.path.dirname(__file__), 'AuditLogs.json')

def log_audit_event(api_key, event):
    audit_entry = {
        "api_key": api_key,
        "event": event,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        with open(AUDIT_LOG_FILE, 'r+') as file:
            data = json.load(file)
            data.append(audit_entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(AUDIT_LOG_FILE, 'w') as file:
            json.dump([audit_entry], file, indent=4)

# Example usage
if __name__ == "__main__":
    log_audit_event("your_api_key_here", "example_event")
