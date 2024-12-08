import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = (
        employee["salary"]
        .drop_duplicates()
        .sort_values(ascending=False)
    )
    
    if N <= 0 or N > len(sorted_salaries):
        nth_salary = None
    else:
        nth_salary = sorted_salaries.iloc[N-1]

    return pd.DataFrame({
        f"getNthHighestSalary({N})": [nth_salary]
    })
