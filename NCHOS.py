# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:09:26 2024

@author: Lin
"""
import requests
import json
import pandas as pd

name = 'North Carolina'
api_url = 'https://api.api-ninjas.com/v1/hospitals?state=NC'
response = requests.get(api_url, headers={'X-Api-Key': 'cChKMU9+fOkY7Mgb08V+sQ==ErF6eyGNpBPb9CuS'})
data = json.loads(response.content)


if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
    
df = pd.json_normalize(data)

with open('NCHOS2.json', 'w') as f:
        json.dump(data,f, indent=2)
        

print(df.shape)
df.to_csv('NCHOS2.csv')

