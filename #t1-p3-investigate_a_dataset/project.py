#!/usr/bin/env python3

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

# create a dataframe from the provided excel
df_gd = pd.read_excel(
    '#t1-p3-investigate_a_dataset/ncis-and-census-data/gun_data.xlsx')
# change dtype of the column 'month'
df_gd['month'] = df_gd['month'].astype('datetime64[ns]')

# create a dataframe based on the census data
# skip last 20 lines because they contain explanations
df_c_raw = pd.read_csv('#t1-p3-investigate_a_dataset/ncis-and-census-data/U.S. Census Data.csv', skipfooter=20, header=0, engine='python')
# drop 'Fact Note' column
df_c_raw = df_c_raw.drop('Fact Note', axis=1)
# setting the index to use "Fact" as keys
df_c_raw.set_index('Fact', inplace=True)

# transpose the dataframe for easier handling
df_c_raw = df_c_raw.transpose()

# replacing commas and turning strings to numbers
df_c_raw['Veterans, 2011-2015'] = df_c_raw['Veterans, 2011-2015'].str.replace(",", "")
# convert to numeric type
df_c_raw['Veterans, 2011-2015'] = pd.to_numeric(df_c_raw['Veterans, 2011-2015'], errors='coerce')

# function to remove '%' and divide by 100
def clean_percentage(x):
    if '%' in x:
        x = x.replace('%', '')
        x = float(x) / 100
        return x
    else:
        return float(x)

# applying the function
df_c_raw['Foreign born persons, percent, 2011-2015'] = df_c_raw['Foreign born persons, percent, 2011-2015'].apply(clean_percentage)

# convert to numeric type
df_c_raw['Foreign born persons, percent, 2011-2015'] = pd.to_numeric(df_c_raw['Foreign born persons, percent, 2011-2015'], errors='coerce')
df_c_raw = df_c_raw.reset_index()

# create a dataframe with the number of permits in 2011 to 2015
permits = (df_gd[df_gd.month.between("2011-01", "2015-12")].groupby("state")["permit"].sum().reset_index())
permits.set_index('state', inplace=True)

# create a dataframe with specific facts
df_t = df_c_raw[['index', 'Veterans, 2011-2015', 'Foreign born persons, percent, 2011-2015']]

# add the number of permits between 2011 and 2015
df_t = df_t.join(permits['permit'], on='index')

df_t[['Veterans, 2011-2015', 'permit']].plot(secondary_y='permit')
#plt.show()

df_t[['Foreign born persons, percent, 2011-2015', 'permit']].plot(secondary_y='permit')
#plt.show()
