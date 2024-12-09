import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = (
        employee["salary"]
        .drop_duplicates()
        .sort_values(ascending=False)
    )

    sec_salary = None
    if len(sorted_salary) >= 2:
        sec_salary = sorted_salary.iloc[1]
    
    return pd.DataFrame({"SecondHighestSalary": [sec_salary]})
