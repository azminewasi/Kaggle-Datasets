import pandas as pd
import datetime
import time

df_2=pd.read_csv("reviews.csv", encoding = "ISO-8859-1")
df=pd.read_csv("data.csv", encoding = "ISO-8859-1")

#df=df[['appId','comments']]

df['appId']=df_2['appId']

print(df.info())
print(df_2.info())

df.to_csv("data.csv",index=False)