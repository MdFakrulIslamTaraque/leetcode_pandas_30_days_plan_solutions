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
-- Write your PostgreSQL query statement below
with combined_info as(
    select
        dp.name as "Department"
        , dp.id as "Dept_id"
        , em.name as "Employee"
        , em.salary as "Salary"
    from
        Employee em
        join Department dp on em.departmentId = dp.id
)
, dept_wise_max_salary as(
    select
        "combined_info"."Department"
        , max("combined_info"."Salary") as "max_sal"
    from
        combined_info
    group by
        1
)
, semi_final as(
    select
        combined_info."Department"
        , combined_info."Employee"
        , combined_info."Salary"
        , dept_wise_max_salary."max_sal"
    from
        combined_info
        join dept_wise_max_salary on combined_info."Department" = dept_wise_max_salary."Department"
)
select
     semi_final."Department"
    , semi_final."Employee"
    , semi_final."Salary"
from
    semi_final
where
    semi_final."Salary" = semi_final."max_sal"
;
