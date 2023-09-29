#I want to clean the columns Street 1 and Street 2 in the file /Users/arthursarazin/Desktop/panneauxM12_geo - panneaux.csv

import pandas as pd
import numpy as np
import re

# Import the file
df = pd.read_csv('/Users/arthursarazin/Desktop/panneauxM12_geo - panneaux.csv', delimiter=';')

# I want to onluy keep the coordinates of the street
df['Street 1'] = df['Street 1'].str.extract(r'(\d+\.\d+,\d+\.\d+)')
df['Street 2'] = df['Street 2'].str.extract(r'(\d+\.\d+,\d+\.\d+)')

#I want to create a new column with the coordinates of the street
df['Street 1'] = df['Street 1'].str.split(',')
df['Street 2'] = df['Street 2'].str.split(',')

# I want a new .csv file with the new columns

df.to_csv('/Users/arthursarazin/Desktop/panneauxM12_geo - panneaux.csv', sep=';')