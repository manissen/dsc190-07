from pathlib import Path
import pandas as pd

input_path = Path("data/clean/events.csv")
output_path = Path("data/transformed/events.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_path)

df["date"] = df["timestamp"].str[:10]

df.to_csv(output_path, index=False)
