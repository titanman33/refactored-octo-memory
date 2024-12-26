# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:18:53 2024

@author: Lin
"""

import pandas as pd

#read contents of local file into a dataframe
df = pd.read_csv(r'C:\Users\Lin\Downloads\nics-firearm-background-checks.csv')

#filters for Alabama rows
alabama_rows = df.loc[df['state'] == 'Alabama']

#writes to delimited file
df.to_csv('CSV/firearm-mdified.csv', sep=',')
alabama_rows.to_csv('CSV/firearm-modified_AL.csv',  sep=',')

print(alabama_rows)