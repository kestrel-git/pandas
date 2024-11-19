import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # student = students[students["student_id"] == 101]
    # return student[["name", "age"]]
    return students.loc[students["student_id"] == 101, ["name", "age"]]
