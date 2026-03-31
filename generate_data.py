import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

pipelines = ["backend", "frontend", "auth-service", "infra"]
statuses = ["success", "failed"]

rows = []
start_date = datetime(2024, 1, 1)

for i in range(300):
    date = start_date + timedelta(days=random.randint(0, 180))
    pipeline = random.choice(pipelines)
    status = random.choices(statuses, weights=[85, 15])[0]
    build_time = round(random.uniform(4, 25), 1)
    failures = 0 if status == "success" else random.randint(1, 5)
    rows.append({
        "date": date.strftime("%Y-%m-%d"),
        "pipeline": pipeline,
        "build_time_mins": build_time,
        "status": status,
        "failures": failures
    })

df = pd.DataFrame(rows)
df = df.sort_values("date").reset_index(drop=True)
df.to_csv("data/deployments.csv", index=False)
print(f"Generated {len(df)} rows -> data/deployments.csv")
