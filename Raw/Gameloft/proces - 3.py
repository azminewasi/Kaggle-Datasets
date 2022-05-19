import pandas as pd
import datetime
import time

df=pd.read_csv("data2.csv", encoding = "ISO-8859-1")
df=df.drop(["icon","androidVersionText"],axis=1)
df['updated'] = df['updated'].apply(lambda d: datetime.date.fromtimestamp(d))
df['released'] = pd.to_datetime(df.released)
df['installs'] = df['installs'].str.replace("-", "")

print(df.info())
print(df.head())

df.to_csv("data3.csv",index=False)