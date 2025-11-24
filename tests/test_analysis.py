import pandas as pd
from src.analysis import summarize_data

def test_summarize_data():
    data = {"A": [1,2,3], "B": [4,5,6]}
    df = pd.DataFrame(data)
    result = summarize_data(df)
    assert result["num_rows"] == 3
    assert result["num_columns"] == 2
    assert "A" in result["columns"]
    assert "B" in result["columns"]