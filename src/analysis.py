import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def summarize_data(df: pd.DataFrame) -> dict:
    summary = {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns)
    }
    return summary

if __name__ == "__main__":
    df = load_data("data/sample.csv")
    print(summarize_data(df))