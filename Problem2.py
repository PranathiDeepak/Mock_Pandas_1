import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:   
    df = my_numbers['num'].value_counts().reset_index()
    df1 = df[df['count'] == 1]
    if df1.empty:
        return pd.DataFrame({'num':[None]})
    else:
        df1 = df1.sort_values(by = 'num', ascending = False)
    return df1.head(1)[['num']]