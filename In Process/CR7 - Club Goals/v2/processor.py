import pandas as pd 

with open("cr7.txt", "r") as data:
    info = data.readlines()
    data.close()

col_name=["Season","Competition","Competition2","Matchday","Date","Venue","Club","Club_Position","Opponent","Opponent_Position","Result","Playing_Position","Minute","At score","Type","Goal_assist"]


numarics="0123456789"

df=[]
second_goal=False
third_goal=False
fourth_goal=False
season=False


for i in range(1,len(info)):
    line=info[i].strip()
    print(line)
    temp=line.split(",")
    
    if "Season " in line:
        season=line.split(" ")[1]
        print("\n\n")
        i=i-1
    
    else:
        temp.insert(0, season)
        
        if temp[1][0] not in numarics:
            if "." not in temp[7]:
                temp.insert(7, "-")
            df.append(temp)
            print(temp)
            second_goal=False
            third_goal=False
            fourth_goal=False
            
        elif second_goal==False:
            temp1=info[i-1].strip().split(",")
            temp1[-4]=temp[1]
            temp1[-3]=temp[2]
            temp1[-2]=temp[3]
            temp1[-1]=temp[4]
            temp1.insert(0, season)
            if "." not in temp1[7]:
                temp1.insert(7, "-")
            df.append(temp1)
            second_goal=True
            print(temp1)
        elif third_goal==False:
            temp1=info[i-2].strip().split(",")
            temp1[-4]=temp[1]
            temp1[-3]=temp[2]
            temp1[-2]=temp[3]
            temp1[-1]=temp[4]
            temp1.insert(0, season)
            if "." not in temp1[7]:
                temp1.insert(7, "-")
            df.append(temp1)
            third_goal=True
            print(temp1)
        elif fourth_goal==False:
            temp1=info[i-3].strip().split(",")
            temp1[-4]=temp[1]
            temp1[-3]=temp[2]
            temp1[-2]=temp[3]
            temp1[-1]=temp[4]
            temp1.insert(0, season)
            if "." not in temp1[7]:
                temp1.insert(7, "-")
            df.append(temp1)
            fourth_goal=True
            print(temp1)
        else:
            temp1=info[i-4].strip().split(",")
            temp1[-4]=temp[1]
            temp1[-3]=temp[2]
            temp1[-2]=temp[3]
            temp1[-1]=temp[4]
            temp1.insert(0, season)
            if "." not in temp1[7]:
                temp1.insert(7, "-")
            df.append(temp1)
            print(temp1)
         
        
df=pd.DataFrame(df,columns=col_name)

print(df)

df.to_csv("data.csv")
