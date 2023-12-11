import pandas as pd

def get_data(PATH):
    df= pd.read_csv(PATH)
    df.dropna(inplace=True)
    medals=df.groupby(["Team", "Medal"])[["Team"]].count()
    medals.rename(columns={"Team":"Count"}, inplace=True)
    medals.reset_index(inplace=True)
    medals.sort_values("Count", ascending=False, inplace= True)
    return medals.iloc[:20]

