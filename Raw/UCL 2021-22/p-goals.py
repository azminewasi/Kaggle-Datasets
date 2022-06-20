import numpy as np 
import pandas as pd

f = open("goals.txt", "r", encoding='utf-8')
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
c12=[]
c13=[]
c14=[]

for i in range(0,len(data),14):
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
    c12.append(data[i+11].strip()) 
    c13.append(data[i+12].strip()) 
    c14.append(data[i+13].strip())
df_dict={"serial":serial,"player_name":player,"club":club,"position":position,"goals":total_attempts,"right_foot":on_target,"left_foot":off_target,"headers":blocked,"others":match_played,"inside_area":c11,"outside_areas":c12,"penalties":c13,"match_played":c14}

df=pd.DataFrame.from_dict(df_dict)
print(df.head())

df.to_csv("goals_o.csv",index=False)