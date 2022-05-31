import numpy as np 
import pandas as pd

f = open("defending.txt", "r", encoding='utf-8')
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
c11=[]

for i in range(0,len(data),11):
    serial.append(data[i+0].strip())
    club.append(data[i+2].strip())
    player.append(data[i+3].strip())
    position.append(data[i+4].split("-")[1].strip())
    total_attempts.append(data[i+5].strip())
    on_target.append(data[i+6].strip())
    off_target.append(data[i+7].strip())
    blocked.append(data[i+8].strip())
    match_played.append(data[i+9].strip())
    c11.append(data[i+10].strip())    
df_dict={"serial":serial,"player_name":player,"club":club,"position":position,"balls_recoverd":total_attempts,"tackles":on_target,"t_won":off_target,"t_lost":blocked,"clearance_attempted":match_played,"match_played":c11}

df=pd.DataFrame.from_dict(df_dict)
print(df.head())

df.to_csv("defending.csv",index=False)