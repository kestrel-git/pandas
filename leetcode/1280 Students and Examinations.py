import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    st_sub_df = students.merge(
        subjects,
        how="cross"
    )

    exams_count_df = (
        examinations
        .groupby(
            by=["student_id", "subject_name"],
            as_index=False
        )
        .agg(attended_exams=("subject_name", "count"))
    )
    
    return (
        st_sub_df
        .merge(
            exams_count_df,
            how="left",
            on=["student_id", "subject_name"]
        )
        .fillna({"attended_exams": 0})
        .sort_values(
            by=["student_id", "subject_name"]
        )
    )
