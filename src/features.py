from pathlib import Path
import pandas as pd

input_path = Path("data/transformed/events.csv")
output_path = Path("data/features/events.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_path)

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

df = df[
    [
        "user_id",
        "timestamp",
        "event_type",
        "duration_seconds",
        "date",
        "duration_minutes",
        "weekday",
    ]
]

df.to_csv(output_path, index=False)
