from pathlib import Path
import pandas as pd

VALID_EVENTS = {"login", "logout", "click", "view", "purchase"}

input_path = Path("data/raw/events.csv")
output_path = Path("data/clean/events.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_path)

df = df.dropna()

df["event_type"] = df["event_type"].astype(str).str.strip()
df = df[df["event_type"].isin(VALID_EVENTS)]

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df[df["duration_seconds"].notna()]
df = df[df["duration_seconds"] > 0]
df = df[df["duration_seconds"] % 1 == 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")
df = df[df["timestamp"].notna()]
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

df = df.dropna()
df = df[["user_id", "timestamp", "event_type", "duration_seconds"]]

df.to_csv(output_path, index=False)


