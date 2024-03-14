# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.

# Write a solution to remove the rows with missing values.

# The result format is in the following example.


# ----------------------------------------------------------------------------------------------------

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(axis = 'index', how = 'any', subset = 'name', inplace = True)
    return students

# or------------------

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # students.dropna(axis = 'index', how = 'any', subset = 'name', inplace = True)
    students.dropna(subset = 'name', inplace = True)
    return students


