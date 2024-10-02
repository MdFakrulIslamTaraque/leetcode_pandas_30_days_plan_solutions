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
