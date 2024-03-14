# Write a solution to correct the errors:

# The grade column is stored as floats, convert it to integers.

# The result format is in the following example.

# -----------------------------------------------------------------------

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df.grade = df.grade.astype(int)
    return df
