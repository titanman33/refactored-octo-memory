# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:09:43 2024

@author: Lin
"""

import json
import pandas as pd
import requests

#data = json.load(open(r'C:\Users\Lin\JSON\RandomUser.json'))
#df = pd.DataFrame(data["results"])

#This works
with open(r'C:/Users/Lin/Toolbox/us_state_capitals.json') as f:
    d = json.load(f)

df2 = pd.json_normalize(d)

#Via API request
url = 'https://api.countrylayer.com/v2/all?access_key=a4fa25d2060bcb54c62f3aea001aa550'
response = requests.get(url)
#use .loads method to convert JSON String into Python object
data = json.loads(response.content)

#dump JSON string into a new file with indent 
with open(r'C:\Users\Lin\JSON\CountryData2.json','w') as f:
    json.dump(data,f, indent=2)  

print(response.status_code)    

#Flattens the data types so it can be managed
df = pd.json_normalize(data)

#Write to delimited file https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv
df.to_csv('CountryData2.csv', sep=',', encoding='utf-8', index=False, header=True)

print(df2)