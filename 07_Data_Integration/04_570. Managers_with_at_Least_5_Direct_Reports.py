"""
link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
"""


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    valid_managers_ids = employee.groupby(['managerId'])['managerId'].count().reset_index(name='manages')
    # managaer_id_df = pd.DataFrame(valid_managers_ids).reset_index()
    ids = valid_managers_ids[valid_managers_ids['manages'] >= 5]['managerId'].to_numpy()
    print(ids)
    return pd.DataFrame(employee[employee['id'].isin(ids)]['name'])