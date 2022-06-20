import numpy as np 
import pandas as pd

df_o=pd.read_csv("key_stats-o.csv")
df_no=pd.read_csv("key_stats - new.csv")
df_o=df_o[df_o['club']!="Real Madrid"]
df_o=df_o[df_o['club']!="Liverpool"]
df_no=df_no.append(df_o, ignore_index=True)
df_no=df_no.drop('serial',axis=1)
print(df_no.info())
df_no.to_csv("key_stats.csv",index=False)