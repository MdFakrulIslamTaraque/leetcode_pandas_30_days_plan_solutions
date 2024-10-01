import pandas as pd
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['population'].values >= 25000000) | ((world['area'].values >= 3000000))][['name', 'population', 'area']]