import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_ids = (
        employee
        .groupby(
            by="managerId", as_index=False)
        .agg(
            reporting=("id", "count")
        )
        .query(
            "reporting >= 5"
        )
        ["managerId"]
    )
    return (
        employee
        [employee["id"].isin(manager_ids)]
        [["name"]]
    )
