import pandas as pd
df=pd.read_csv("data.csv")
df=df.drop(["Competition2","Club_Position","Opponent_Position"],axis=1)
df=df.rename(columns={"At score": "At_score"})
print(df.head())
df.to_csv("data.csv")