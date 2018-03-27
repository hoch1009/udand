#!/usr/bin/env python3

import numpy as np
import pandas as pd
import re
#import matplotlib.pylot as plt

# create a dataframe from the provided excel
df_gun_data = pd.read_excel('#t1-p3-investigate_a_dataset/ncis-and-census-data/gun_data.xlsx')
# change dtype of the column 'month'
df_gun_data['month'] = df_gun_data['month'].astype('datetime64[ns]')

# skip last 20 lines because they contain explanations
df_census_raw = pd.read_csv('#t1-p3-investigate_a_dataset/ncis-and-census-data/U.S. Census Data.csv', skipfooter=20, header=0, engine='python')
# drop 'Fact Note' column
df_census_raw = df_census_raw.drop('Fact Note', axis=1)
# setting the index to use "Fact" as keys
df_census_raw.set_index('Fact', inplace=True)
# transpose the dataframe for easier handling
df_census_raw = df_census_raw.transpose()

# replacing commas and turning strings to numbers
df_census_raw['Veterans, 2011-2015'] = df_census_raw['Veterans, 2011-2015'].str.replace(",", "")
# convert to numeric type
df_census_raw['Veterans, 2011-2015'] = pd.to_numeric(df_census_raw['Veterans, 2011-2015'], errors='coerce')

# remove '%' and divide by 100
def clean_percentage(x):
    if '%' in x:
        x = x.replace('%', '')
        x = float(x)/100
        return x
    else:
        return float(x)

# applying the function
df_census_raw['Foreign born persons, percent, 2011-2015'] = df_census_raw['Foreign born persons, percent, 2011-2015'].apply(clean_percentage)

# convert to numeric type
df_census_raw['Foreign born persons, percent, 2011-2015'] = pd.to_numeric(df_census_raw['Foreign born persons, percent, 2011-2015'], errors='coerce')

# create dataframes to check for correlation
df_census1 = pd.concat([df_census_raw['Veterans, 2011-2015'].nlargest(5),
                         df_census_raw['Veterans, 2011-2015'].nsmallest(5)],
                         keys=['h_pct_veterans', 'l_pct_veterans']).to_frame()

df_census2 = pd.concat([df_census_raw['Foreign born persons, percent, 2011-2015'].nlargest(5),
                        df_census_raw['Foreign born persons, percent, 2011-2015'].nsmallest(5)],
                        keys=['h_pct_foreigners', 'l_pct_foreigners']).to_frame()

total_number_of_permits_2011_2015 = df_gun_data['permit'][(df_gun_data['month'] >= '2011-01-01') & (df_gun_data['month'] <= '2015-12-31')].sum()
print(total_number_of_permits_2011_2015)

# TODO: include condition 'state' in calculation for permit
