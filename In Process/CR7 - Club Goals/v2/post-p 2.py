import pandas as pd
df=pd.read_csv("data.csv")
df=df.drop(["id","id2"],axis=1)
print(df.head())
df.to_csv("data.csv",index=False)