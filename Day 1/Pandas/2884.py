# Write a solution to modify the salary column by multiplying each salary by 2.

# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# Explanation:
# Every salary has been doubled.

# ----------------------------------------------------------------------------------------------

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary = 2 * employees.salary
    return employees

