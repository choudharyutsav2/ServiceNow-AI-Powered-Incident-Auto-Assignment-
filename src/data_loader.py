import pandas as pd

def load_incidents(path):
    df = pd.read_csv(path)
    df = df.fillna("")

    df["combined_text"] = (
        df["short_description"] + " " +
        df["category"] + " " +
        df["cmdb_ci"] + " " +
        df["description"]
    )

    return df
