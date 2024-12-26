# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:42:34 2024

@author: Lin
"""

import json
import pandas as pd
import requests

url = 'https://data.epa.gov/efservice/lookups.mv_new_geo_best_picks/state_code/equals/NC/join/frs.frs_program_facility/registry_id/equals/registry_id/pgm_sys_acrnm/equals/ICIS'
response = requests.get(url)
data = json.loads(response.content)

with open ('WeDontKnow.json', 'w') as f:
    json.dump(data,f,indent=2)

df = pd.json_normalize(data)

our_zip = df.loc[df['postal_code'] == '28105']

our_zip.to_csv('WeDontKnow.csv')

print(our_zip)