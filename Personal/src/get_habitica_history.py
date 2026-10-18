import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

USER_ID = os.environ["HABITICA_USER_ID"]
API_TOKEN = os.environ["HABITICA_API_TOKEN"]

headers = {
    "x-api-user": USER_ID,
    "x-api-key": API_TOKEN,
    "x-client": f"{USER_ID}-PersonalDashboard"
}

url = "https://habitica.com/api/v3/tasks/user"

response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()

tasks = response.json()["data"]

# Extract historical observations
history = []

for task in tasks:
    for entry in task.get("history", []):
        history.append({
            "task_id": task["id"],
            "task_name": task["text"],
            "task_type": task["type"],
            "date": entry.get("date"),
            "value": entry.get("value")
        })

df_history = pd.DataFrame(
    history,
    columns=["task_id", "task_name", "task_type", "date", "value"]
)

# Convert timestamps
df_history["date"] = pd.to_datetime(
    df_history["date"],
    unit="ms",
    utc=True,
    errors="coerce"
)

print(df_history.head())
# Save to csv file
df_history.to_csv("data/habitica_task_history.csv", index=False)
df_tasks = pd.json_normalize(tasks)
df_tasks.to_csv("data/habitica_tasks.csv", index=False)