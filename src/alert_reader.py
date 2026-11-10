
import json
from collections import deque

alert_file = "/var/ossec/logs/alerts/alerts.json"

with open(alert_file, "r") as file:
    alerts = deque(file, maxlen=5)

print("\nWAZUH SECURITY ALERTS")
print("=" * 40)

for alert in alerts:
    data = json.loads(alert)
    rule = data.get("rule", {})

    print("Timestamp:", data.get("timestamp"))
    print("Severity:", rule.get("level"))
    print("Rule ID:", rule.get("id"))
    print("Description:", rule.get("description"))
    print("-" * 40)
