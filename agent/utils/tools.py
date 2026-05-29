import pandas as pd
from state import AgentState


def load_data(CSV_PATH):
    
    """Loads the CSV data into the state."""
    df = pd.read_csv(CSV_PATH)
    print(df)
    return df