#!/usr/bin/env python3

import numpy as np
import pandas as pd
import re
#import matplotlib.pylot as plt

# create a dataframe from the provided excel
df_gd = pd.read_excel(
    '#t1-p3-investigate_a_dataset/ncis-and-census-data/gun_data.xlsx')
# change dtype of the column 'month'
df_gd['month'] = df_gd['month'].astype('datetime64[ns]')

# create a dataframe based on the census data
# skip last 20 lines because they contain explanations
df_c_raw = pd.read_csv(
    '#t1-p3-investigate_a_dataset/ncis-and-census-data/U.S. Census Data.csv', skipfooter=20, header=0, engine='python')
# drop 'Fact Note' column
df_c_raw = df_c_raw.drop('Fact Note', axis=1)
# setting the index to use "Fact" as keys
df_c_raw.set_index('Fact', inplace=True)
# transpose the dataframe for easier handling
df_c_raw = df_c_raw.transpose()

# replacing commas and turning strings to numbers
df_c_raw[
    'Veterans, 2011-2015'] = df_c_raw['Veterans, 2011-2015'].str.replace(",", "")
# convert to numeric type
df_c_raw['Veterans, 2011-2015'] = pd.to_numeric(
    df_c_raw['Veterans, 2011-2015'], errors='coerce')

# function to remove '%' and divide by 100
def clean_percentage(x):
    if '%' in x:
        x = x.replace('%', '')
        x = float(x) / 100
        return x
    else:
        return float(x)

# applying the function
df_c_raw['Foreign born persons, percent, 2011-2015'] = df_c_raw[
    'Foreign born persons, percent, 2011-2015'].apply(clean_percentage)

# convert to numeric type
df_c_raw['Foreign born persons, percent, 2011-2015'] = pd.to_numeric(
    df_c_raw['Foreign born persons, percent, 2011-2015'], errors='coerce')

# create dataframes including the states with the highest and lowest number of veterans
df_c1 = pd.concat([df_c_raw['Veterans, 2011-2015'].nlargest(5),
                   df_c_raw['Veterans, 2011-2015'].nsmallest(5)],
                  keys=['h_pct_vet', 'l_pct_vet'], names=['category', 'state']).to_frame().reset_index()

# create dataframes including the states with the highest and lowest number of forein born persons
df_c2 = pd.concat([df_c_raw['Foreign born persons, percent, 2011-2015'].nlargest(5),
                   df_c_raw['Foreign born persons, percent, 2011-2015'].nsmallest(5)],
                  keys=['h_pct_foreigners', 'l_pct_foreigners'], names=['category', 'state']).to_frame().reset_index()

# create a dataframe with the number of permits in 2011 to 2015
permits = (df_gd[df_gd.month.between("2011-01", "2015-12")
                 ].groupby("state")["permit"].sum().reset_index())
permits.set_index('state', inplace=True)

# merge the dataframes to check if the selected census data does correlate with high number of permits
df_c1 = df_c1.merge(permits, left_on="state", right_index=True, how="left")
df_c2 = df_c2.merge(permits, left_on="state", right_index=True, how="left")
