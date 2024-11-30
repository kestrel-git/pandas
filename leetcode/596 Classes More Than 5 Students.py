import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt_courses = (
        courses
        .groupby("class", as_index=False)
        .count()
    )
    return cnt_courses[cnt_courses["student"] >= 5][["class"]]
