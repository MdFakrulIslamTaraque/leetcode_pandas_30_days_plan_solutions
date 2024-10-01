import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'user_id':users['user_id'],'name':users['name'].str.capitalize()}).sort_values(by='user_id')