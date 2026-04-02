import pandas as pd
import json

def read_csv(path):
    return pd.read_csv(path)

def write_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def write_csv(df, path):
    df.to_csv(path, index=False)