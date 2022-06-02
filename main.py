import re
import requests  #for making standard html requests
from bs4 import BeautifulSoup  #magical tool for parsing html data

import pandas as pd
url = 'https://www.tenable.com/plugins/nessus/families/AIX%20Local%20Security%20Checks'

tenablePage = requests.get(url)

html_soup = BeautifulSoup(tenablePage.content, 'html.parser')


result = html_soup.find_all("a", attrs= {"href": re.compile('\d{5,6}')})

url = []
id = []

#go through result and get url 
for x in result:
  y = str(x).split('"',2)
  url.append(y[1])
  #id.append()
  print("URL:", y[1])

     
#go through result and get id
for x in url:
  y = x.split('/',5)
  id.append(y[5])
  print("ID:", y[5])
     
# dictionary for csv  
dict = {'ID': id, 'URL': url}  


df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('Result.csv') 
