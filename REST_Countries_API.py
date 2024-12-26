# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:38:03 2024

@author: Lin
"""
import json
import pandas as pd
import requests

url = 'https://restcountries.com/v3.1/all?fields='
#key = '?access_key=a4fa25d2060bcb54c62f3aea001aa550'
fields = 'name,area,capital,fifa,languages,population,timezones,unMember'

qual_url = url+fields
#auth_url = url+key

response = requests.get(qual_url)
data = json.loads(response.content)

with open ('JSON/CountryData3.json', 'w') as f:
    json.dump(data,f,indent=2)
 
#Flattens the data types so it can be managed
df = pd.json_normalize(data)
small_countries = df.loc[df['population'] < 1000]
spanish_countries = df.loc[df['languages.spa'] == 'Spanish']
pretty_df = df[['name.common','capital','population','area']]

#Write to delimited file https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv
#small_countries.to_csv('CSV/CountryData_Small.csv', sep=',', encoding='utf-8', index=False, header=True)

#spanish_countries.to_csv('CSV/CountryData_Small.csv', sep=',', encoding='utf-8', index=False, header=True)


#print(qual_url)    
#print(response.status_code)
print(spanish_countries)

#print(response.status_code)
#print(data)