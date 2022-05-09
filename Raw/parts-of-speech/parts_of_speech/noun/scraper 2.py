from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print("Persed")

adj= []
   
#Quotes Section
products = soup.select('td>a')
for elems in products:
    adj.append(elems.text.strip())


with open('noun 2.txt', 'w') as f:
    for item in adj:
        f.write("%s\n" % item)
        print(item)