from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://7esl.com/english-verbs/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

verbs= []
   
#Quotes Section
products = soup.select('ul>li')
for elems in products:
    verbs.append(elems.text.strip())


with open('verb.txt', 'w') as f:
    for item in verbs:
        f.write("%s\n" % item)
        print(item)