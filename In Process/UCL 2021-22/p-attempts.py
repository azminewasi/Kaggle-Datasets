import numpy as np 
import pandas as pd

f = open("attempts.txt", "r", encoding='utf-8')
data=f.readlines()


serial=[]
player=[]
club=[]
position=[]
total_attempts=[]
on_target=[]
off_target=[]
blocked=[]
match_played=[]

for i in range(0,len(data),10):
    serial.append(data[i+0].strip())
    club.append(data[i+2].strip())
    player.append(data[i+3].strip())
    position.append(data[i+4].split("-")[1].strip())
    total_attempts.append(data[i+5].strip())
    on_target.append(data[i+6].strip())
    off_target.append(data[i+7].strip())
    blocked.append(data[i+8].strip())
    match_played.append(data[i+9].strip())
    
df_dict={"serial":serial,"player_name":player,"club":club,"position":position,"total_attempts":total_attempts,"on_target":on_target,"off_target":off_target,"blocked":blocked,"match_played":match_played}

df=pd.DataFrame.from_dict(df_dict)
print(df.head())

df.to_csv("attempts.csv",index=False)