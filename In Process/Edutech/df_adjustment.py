import pandas as pd

df=pd.read_csv("data-un.csv")

df=df.drop(["price","free","currency","sale","saleTime","originalPrice","saleText","offersIAP","inAppProductPrice","androidVersionText","description","descriptionHTML","summaryHTML","histogram","minInstalls","developerEmail","developerWebsite","developerAddress","privacyPolicy","developerInternalID","headerImage","screenshots","video","videoImage","contentRatingDescription","adSupported","recentChanges","recentChangesHTML","editorsChoice","moreByDeveloper","appId"],axis=1)

df['installs'] = df['installs'].str[:-1]
df['installs'] .replace(',','', regex=True, inplace=True)

df.info()

df.to_csv("edtech%20platform - data.csv")