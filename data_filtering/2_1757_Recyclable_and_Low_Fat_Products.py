import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(products[(products['low_fats'].values=='Y') & (products['recyclable'].values=='Y')]['product_id'])