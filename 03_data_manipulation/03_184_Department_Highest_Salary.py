"""
link: https://leetcode.com/problems/department-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

"""


import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # merge 2 df using inner join
    employee_merged_dept = pd.merge(employee, department, how='inner', left_on=['departmentId'], right_on=['id'])
    
    # get the max salary of each dept., put it in a separate df, which will be used to be merged late
    dept_max_sal = employee_merged_dept.groupby(['departmentId'], as_index=False).max()
    dept_max_sal_final = pd.DataFrame({'Department':dept_max_sal['name_y'], 'Salary':dept_max_sal['salary']})

    # get a df group by dept_id and emp_id to get the duplicates 
    res_df = employee_merged_dept.groupby(['departmentId','id_x'], as_index=False).max()
    res_final = pd.DataFrame({'Department':res_df['name_y'], 'Employee':res_df['name_x'], 'Salary':res_df['salary']})
    res_final.sort_values(by=['Department','Salary'], ascending=[True, False])

    # then finally merge the 2 df from group by results, to get all the max salary(s) of each dept
    ans_res_df = pd.merge(res_final, dept_max_sal_final, how='inner', on=['Department', 'Salary'])
    return ans_res_df
