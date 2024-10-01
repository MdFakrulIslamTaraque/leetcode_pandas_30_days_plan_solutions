import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'id':views[views['author_id'] == views['viewer_id']].sort_values(by='author_id')['author_id'].unique()})