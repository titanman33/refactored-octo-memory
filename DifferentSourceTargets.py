# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:29:27 2024

@author: Lin
"""

import pandas as pd

#get the file from a distinct filepath
df = pd.read_csv(r'C:\Users\Lin\Downloads\capitals.csv')

#writes the dataframe to a CSV file
#df.to_csv('CSV/modified.csv')

#writes to a tab delimited file
#df.to_csv('CSV/tabmodified.tsv', sep='\t')

#writes to a tab delimited file
#df.to_csv('CSV/semicolonmodified.csv', sep=';')

#writes to a tab delimited file
#df.to_csv('CSV/pipemodified.csv', sep='|')

#writes to a JSON file
#df.to_json('JSON/modified.json')

#makes the response more readable
#df.to_json('JSON/modified.json', orient='records', lines=True)

#reads in the JSON file
#test = pd.read_json('JSON/modified.json', orient='records', lines=True)
#print(test.head())

#read from a Postgres Database
#watch this: https://youtu.be/N6hyN6BW6ao?si=0em0j0d892TD5g7p&t=1166

#pip install SQLAlchemy
#pip install psycopg2-binary

import requests
import json

url = 'https://randomuser.me/api'

response = requests.get(url)
#use .loads method to convert JSON String into Python object
data = json.loads(response.content)

#dump JSON string into a new file with indent 
with open(r'C:\Users\Lin\JSON/randomUser.json','w') as f:
    json.dump(data,f, indent=2)    
