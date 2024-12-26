# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:11:44 2024

@author: Lin
"""

import json
import requests
import pandas as pd

#From API-Ninjas 
url = 'https://api.api-ninjas.com/v1/city?country=US&limit=30&min_population=30000&max_population=900000'
response = requests.get(url, headers={'X-Api-Key': 'cChKMU9+fOkY7Mgb08V+sQ==ErF6eyGNpBPb9CuS'})
data = json.loads(response.content)

if response.status_code == requests.codes.ok:
    print(response.content)
else:
    print("Error:", response.status_code, response.text)    

with open('Medium_Cities.json', 'w') as f:
        json.dump(data,f, indent=2)
        
df = pd.json_normalize(data)

df.to_csv('Medium_Cities.csv')