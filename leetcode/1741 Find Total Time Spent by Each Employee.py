import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_spent"] = employees["out_time"] - employees["in_time"]
    return (
        employees
        .groupby(by=["event_day", "emp_id"], as_index=False)
        ["time_spent"]
        .sum()
        .rename(columns={"event_day": "day", "time_spent": "total_time"})
    )
