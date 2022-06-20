import pandas as pd 

with open("Goals.csv", "r") as data:
    info = data.readlines()
    data.close()


numarics="0123456789"

df=[]
second_goal=False
third_goal=False
fourth_goal=False


for i in range(1,len(info)):
    line=info[i].strip()
    temp=line.split(",")
    
    if temp[1]!="":
        if temp[1][0] not in numarics:
            temp.insert(0, i)
            df.append(temp)
            second_goal=False
            third_goal=False
            fourth_goal=False
            
        elif second_goal==False:
            temp1=info[i-1].strip().split(",")
            temp1[8]=temp[1]
            temp1[9]=temp[2]
            temp1[10]=temp[3]
            temp1.insert(0, i)
            df.append(temp1)
            second_goal=True
        elif third_goal==False:
            temp1=info[i-2].strip().split(",")
            temp1[8]=temp[1]
            temp1[9]=temp[2]
            temp1[10]=temp[3]
            temp1.insert(0, i)
            df.append(temp1)
            third_goal=True
        elif fourth_goal==False:
            temp1=info[i-3].strip().split(",")
            temp1[8]=temp[1]
            temp1[9]=temp[2]
            temp1[10]=temp[3]
            temp1.insert(0, i)
            df.append(temp1)
            fourth_goal=True
        else:
            temp1=info[i-4].strip().split(",")
            temp1[8]=temp[1]
            temp1[9]=temp[2]
            temp1[10]=temp[3]
            temp1.insert(0, i)
            df.append(temp1)
    else:
         temp1=info[i-1].strip().split(",")
         temp1[8]=temp[8]
         temp1[9]=temp[9]
         temp1[10]=temp[10]
         temp1.insert(0, i)
         df.append(temp1)
         
        
df=pd.DataFrame(df,columns=["Goal_no","Season","Competition","Matchday","Venue","Team","Opponent","Result","Position","Minute","At_score","Type_of_goal"])

print(df)

df.to_csv("data.csv",index_row=False)