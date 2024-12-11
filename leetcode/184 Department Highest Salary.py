import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return (
        employee
        .groupby("departmentId", group_keys=False)
        .apply(lambda x: x[x["salary"] == x["salary"].max()])
        .reset_index(drop=True)
        .merge(
            department,
            left_on="departmentId",
            right_on="id",
            suffixes=("_em", "_dp")
        )
        .rename(columns={
            "name_dp": "Department",
            "name_em": "Employee",
            "salary": "Salary"
        })
        [["Department", "Employee", "Salary"]]
    )
