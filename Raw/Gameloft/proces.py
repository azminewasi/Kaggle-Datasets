import pandas as pd
df=pd.read_csv("data.csv", encoding = "ISO-8859-1")
df=df.drop(["id","genre","contentRatingDescription"],axis=1)
df['installs'] = df['installs'].str[:-1]
df['installs'] = df['installs'].str.replace("-", "")
df['genreId'] = df['genreId'].str[5:]
print(df.info())
df.to_csv("data2.csv",index=False)

#data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d))