import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    bonus_ids = employees[(employees['employee_id']%2 == 1) & (employees['name'].str.get(0) != 'M')]['employee_id']
    no_bonus_ids = employees['employee_id'].isin(bonus_ids)
    bonus_ids.to_numpy()
    res_df = pd.DataFrame({'employee_id':employees['employee_id'], 'bonus_check':no_bonus_ids})
    res_df['bonus'] = np.where(res_df['bonus_check'] == True, employees['salary'], 0)
    return res_df[['employee_id', 'bonus']].sort_values(by='employee_id')