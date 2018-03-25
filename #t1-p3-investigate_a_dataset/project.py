#!/usr/bin/env python3

import numpy as np
import pandas as pd
#import matplotlib.pylot as plt

#import os
#print(os.getcwd())


df1 = pd.read_excel('#t1-p3-investigate_a_dataset/ncis-and-census-data/gun_data.xlsx')

# skip last 20 lines because they contain explanations
df2 = pd.read_csv('#t1-p3-investigate_a_dataset/ncis-and-census-data/U.S. Census Data.csv', skipfooter=20, header=0)
# drop 'Fact Note' column
df2 = df2.drop('Fact Note', axis=1)
# setting the index to use "Fact" as keys
df2.set_index('Fact', inplace=True)
# transpose the dataframe for easier handling
df2 = df2.transpose()

# replacing commas and turning strings to numbers
df2['Veterans, 2011-2015'] = df2['Veterans, 2011-2015'].str.replace(",", "")
df2['Veterans, 2011-2015'] = pd.to_numeric(df2['Veterans, 2011-2015'], errors='coerce')

# get the 5 states with the largest and smallest amount of veterans
print(df2['Veterans, 2011-2015'].nlargest(5))
print(df2['Veterans, 2011-2015'].nsmallest(5))

# TODO: data wrangling
df2['Foreign born persons, percent, 2011-2015']

# TODO: get the 5 states with the largest and smallest percentage of forein born persons
print(df2['Foreign born persons, percent, 2011-2015'].nlargest(5))
print(df2['Foreign born persons, percent, 2011-2015'].nsmallest(5))

# TODO: check if there is a correlation between the two
