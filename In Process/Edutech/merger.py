import pandas as pd
csv_list=["byju&c=apps - data.csv","course&c=apps - data.csv","edtech%20platform - data.csv","educational%20apps - data.csv"]

df=pd.read_csv(csv_list[0])

for i in range(1,len(csv_list)):
    temp=pd.read_csv(csv_list[i])
    df=pd.concat([df,temp])

print(df.info())


df= df.drop_duplicates(subset='title')

print(df)

df=df.sort_values('installs', ascending=False)

df=df.drop(["Unnamed: 0","Unnamed: 0.1","genre","developerId"],axis=1)
df = df.drop(df[df['genreId']!='EDUCATION'].index)
#df = df.drop(df[df['score']<1.00].index)


df=df.reset_index(drop=True)

print(df.info())

reviews=df[["title","url","comments"]]

df=df.drop(["comments"],axis=1)
df.to_csv("merged - data.csv",index=False)
reviews.to_csv("review - data.csv",index=False)

print(len(reviews['comments'][6]))