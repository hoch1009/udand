
# Investigating gun data in the U.S.

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<ul>
<li><a href='#wrangling_gd'>Data Cleaning (gun_data.xlsx)</a></li>
<li><a href='#wrangling_cd'>Data Cleaning (U.S. Census Data.csv)</a></li>
</ul>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<ul>
<li><a href='q1'>Q1: Does the number of veterans per state affect the number of gun purchases?</a></li>
<li><a href='q2'>Q2: Does the number of foreign born persons per state affect the number of gun purchases?</a></li>
<li><a href='q3'>Q3: What is the overall trend of gun purchases?</a></li></ul>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id='intro'></a>
## Introduction

The following analysis is based on data from the FBI's National Instant Criminal Background Check System which can be found on [GitHub](https://github.com/BuzzFeedNews/nics-firearm-background-checks/blob/master/README.md). The data set consists of two files:
- **gun_data.xlsx**: containing the actual gun data per state per month
- **U.S. Census Data.csv**: containing some variables on state level which can be used to investigate if certain aspects have an effect on the number of guns per state


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
```


```python
# Create a dataframe based on the gun_data.xlsx
df_gd = pd.read_excel('gun_data.xlsx')

# Create a dataframe based on the raw census data
df_c_raw = pd.read_csv('U.S. Census Data.csv')
```

<a id='wrangling'></a>
## Data Wrangling

### General Properties of the file: gun_data.xlsx

Getting a general overview over the data:


```python
df_gd.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 12485 entries, 0 to 12484
    Data columns (total 27 columns):
    month                        12485 non-null object
    state                        12485 non-null object
    permit                       12461 non-null float64
    permit_recheck               1100 non-null float64
    handgun                      12465 non-null float64
    long_gun                     12466 non-null float64
    other                        5500 non-null float64
    multiple                     12485 non-null int64
    admin                        12462 non-null float64
    prepawn_handgun              10542 non-null float64
    prepawn_long_gun             10540 non-null float64
    prepawn_other                5115 non-null float64
    redemption_handgun           10545 non-null float64
    redemption_long_gun          10544 non-null float64
    redemption_other             5115 non-null float64
    returned_handgun             2200 non-null float64
    returned_long_gun            2145 non-null float64
    returned_other               1815 non-null float64
    rentals_handgun              990 non-null float64
    rentals_long_gun             825 non-null float64
    private_sale_handgun         2750 non-null float64
    private_sale_long_gun        2750 non-null float64
    private_sale_other           2750 non-null float64
    return_to_seller_handgun     2475 non-null float64
    return_to_seller_long_gun    2750 non-null float64
    return_to_seller_other       2255 non-null float64
    totals                       12485 non-null int64
    dtypes: float64(23), int64(2), object(2)
    memory usage: 2.6+ MB


**Observations:**
- The column 'month' has an incorrect datatype (_object_ instead of _datetime64[ns]_)

### General Properties of the file: U.S. Census Data.csv

Getting a general overview over the data:


```python
df_c_raw.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 85 entries, 0 to 84
    Data columns (total 52 columns):
    Fact              80 non-null object
    Fact Note         28 non-null object
    Alabama           65 non-null object
    Alaska            65 non-null object
    Arizona           65 non-null object
    Arkansas          65 non-null object
    California        65 non-null object
    Colorado          65 non-null object
    Connecticut       65 non-null object
    Delaware          65 non-null object
    Florida           65 non-null object
    Georgia           65 non-null object
    Hawaii            65 non-null object
    Idaho             65 non-null object
    Illinois          65 non-null object
    Indiana           65 non-null object
    Iowa              65 non-null object
    Kansas            65 non-null object
    Kentucky          65 non-null object
    Louisiana         65 non-null object
    Maine             65 non-null object
    Maryland          65 non-null object
    Massachusetts     65 non-null object
    Michigan          65 non-null object
    Minnesota         65 non-null object
    Mississippi       65 non-null object
    Missouri          65 non-null object
    Montana           65 non-null object
    Nebraska          65 non-null object
    Nevada            65 non-null object
    New Hampshire     65 non-null object
    New Jersey        65 non-null object
    New Mexico        65 non-null object
    New York          65 non-null object
    North Carolina    65 non-null object
    North Dakota      65 non-null object
    Ohio              65 non-null object
    Oklahoma          65 non-null object
    Oregon            65 non-null object
    Pennsylvania      65 non-null object
    Rhode Island      65 non-null object
    South Carolina    65 non-null object
    South Dakota      65 non-null object
    Tennessee         65 non-null object
    Texas             65 non-null object
    Utah              65 non-null object
    Vermont           65 non-null object
    Virginia          65 non-null object
    Washington        65 non-null object
    West Virginia     65 non-null object
    Wisconsin         65 non-null object
    Wyoming           65 non-null object
    dtypes: object(52)
    memory usage: 34.6+ KB


**Observations:**
- The column 'Fact Note' can be dropped.
- The last 20 rows of the file contain explanations and can be dropped.
- The columns and rows are switched (rows contain variables and the columns contain the states).

<a id='wrangling_gd'></a>
### Data Cleaning (gun_data.xlsx)


```python
# change dtype of the column 'month'
df_gd['month'] = df_gd['month'].astype('datetime64[ns]')
```

<a id='wrangling_cd'></a>
### Data Cleaning (U.S. Census Data.csv)


```python
# create dataframe and skip last 20 lines
df_c_raw = pd.read_csv('U.S. Census Data.csv', skipfooter=20, header=0, engine='python')
```


```python
# drop 'Fact Note' column
df_c_raw = df_c_raw.drop('Fact Note', axis=1)
```


```python
# setting the index to use "Fact" as keys
df_c_raw.set_index('Fact', inplace=True)
```


```python
# transpose the dataframe for easier handling
df_c_raw = df_c_raw.transpose()
```


```python
# get info about the new dataframe
df_c_raw.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 50 entries, Alabama to Wyoming
    Data columns (total 65 columns):
    Population estimates, July 1, 2016,  (V2016)                                              50 non-null object
    Population estimates base, April 1, 2010,  (V2016)                                        50 non-null object
    Population, percent change - April 1, 2010 (estimates base) to July 1, 2016,  (V2016)     50 non-null object
    Population, Census, April 1, 2010                                                         50 non-null object
    Persons under 5 years, percent, July 1, 2016,  (V2016)                                    50 non-null object
    Persons under 5 years, percent, April 1, 2010                                             50 non-null object
    Persons under 18 years, percent, July 1, 2016,  (V2016)                                   50 non-null object
    Persons under 18 years, percent, April 1, 2010                                            50 non-null object
    Persons 65 years and over, percent,  July 1, 2016,  (V2016)                               50 non-null object
    Persons 65 years and over, percent, April 1, 2010                                         50 non-null object
    Female persons, percent,  July 1, 2016,  (V2016)                                          50 non-null object
    Female persons, percent, April 1, 2010                                                    50 non-null object
    White alone, percent, July 1, 2016,  (V2016)                                              50 non-null object
    Black or African American alone, percent, July 1, 2016,  (V2016)                          50 non-null object
    American Indian and Alaska Native alone, percent, July 1, 2016,  (V2016)                  50 non-null object
    Asian alone, percent, July 1, 2016,  (V2016)                                              50 non-null object
    Native Hawaiian and Other Pacific Islander alone, percent, July 1, 2016,  (V2016)         50 non-null object
    Two or More Races, percent, July 1, 2016,  (V2016)                                        50 non-null object
    Hispanic or Latino, percent, July 1, 2016,  (V2016)                                       50 non-null object
    White alone, not Hispanic or Latino, percent, July 1, 2016,  (V2016)                      50 non-null object
    Veterans, 2011-2015                                                                       50 non-null object
    Foreign born persons, percent, 2011-2015                                                  50 non-null object
    Housing units,  July 1, 2016,  (V2016)                                                    50 non-null object
    Housing units, April 1, 2010                                                              50 non-null object
    Owner-occupied housing unit rate, 2011-2015                                               50 non-null object
    Median value of owner-occupied housing units, 2011-2015                                   50 non-null object
    Median selected monthly owner costs -with a mortgage, 2011-2015                           50 non-null object
    Median selected monthly owner costs -without a mortgage, 2011-2015                        50 non-null object
    Median gross rent, 2011-2015                                                              50 non-null object
    Building permits, 2016                                                                    50 non-null object
    Households, 2011-2015                                                                     50 non-null object
    Persons per household, 2011-2015                                                          50 non-null object
    Living in same house 1 year ago, percent of persons age 1 year+, 2011-2015                50 non-null object
    Language other than English spoken at home, percent of persons age 5 years+, 2011-2015    50 non-null object
    High school graduate or higher, percent of persons age 25 years+, 2011-2015               50 non-null object
    Bachelor's degree or higher, percent of persons age 25 years+, 2011-2015                  50 non-null object
    With a disability, under age 65 years, percent, 2011-2015                                 50 non-null object
    Persons  without health insurance, under age 65 years, percent                            50 non-null object
    In civilian labor force, total, percent of population age 16 years+, 2011-2015            50 non-null object
    In civilian labor force, female, percent of population age 16 years+, 2011-2015           50 non-null object
    Total accommodation and food services sales, 2012 ($1,000)                                50 non-null object
    Total health care and social assistance receipts/revenue, 2012 ($1,000)                   50 non-null object
    Total manufacturers shipments, 2012 ($1,000)                                              50 non-null object
    Total merchant wholesaler sales, 2012 ($1,000)                                            50 non-null object
    Total retail sales, 2012 ($1,000)                                                         50 non-null object
    Total retail sales per capita, 2012                                                       50 non-null object
    Mean travel time to work (minutes), workers age 16 years+, 2011-2015                      50 non-null object
    Median household income (in 2015 dollars), 2011-2015                                      50 non-null object
    Per capita income in past 12 months (in 2015 dollars), 2011-2015                          50 non-null object
    Persons in poverty, percent                                                               50 non-null object
    Total employer establishments, 2015                                                       50 non-null object
    Total employment, 2015                                                                    50 non-null object
    Total annual payroll, 2015 ($1,000)                                                       50 non-null object
    Total employment, percent change, 2014-2015                                               50 non-null object
    Total nonemployer establishments, 2015                                                    50 non-null object
    All firms, 2012                                                                           50 non-null object
    Men-owned firms, 2012                                                                     50 non-null object
    Women-owned firms, 2012                                                                   50 non-null object
    Minority-owned firms, 2012                                                                50 non-null object
    Nonminority-owned firms, 2012                                                             50 non-null object
    Veteran-owned firms, 2012                                                                 50 non-null object
    Nonveteran-owned firms, 2012                                                              50 non-null object
    Population per square mile, 2010                                                          50 non-null object
    Land area in square miles, 2010                                                           50 non-null object
    FIPS Code                                                                                 50 non-null object
    dtypes: object(65)
    memory usage: 25.8+ KB


**I choose to investigate the variables 'Veterans, 2011-2015' and 'Foreign born persons, percent, 2011-2015' further.**


```python
# print out all values
df_c_raw['Veterans, 2011-2015']
```




    Alabama             363,170
    Alaska               69,323
    Arizona             505,794
    Arkansas            220,953
    California        1,777,410
    Colorado            391,725
    Connecticut         199,331
    Delaware             71,213
    Florida           1,507,738
    Georgia             670,617
    Hawaii              110,238
    Idaho               119,711
    Illinois            668,933
    Indiana             426,493
    Iowa                211,066
    Kansas              198,396
    Kentucky            297,312
    Louisiana           281,989
    Maine               119,058
    Maryland            403,900
    Massachusetts       355,083
    Michigan            626,722
    Minnesota           342,388
    Mississippi         184,774
    Missouri            451,342
    Montana              90,000
    Nebraska            132,918
    Nevada              220,332
    New Hampshire       106,827
    New Jersey          393,277
    New Mexico           164157
    New York             828586
    North Carolina       696119
    North Dakota          51179
    Ohio                 806531
    Oklahoma             295847
    Oregon               306723
    Pennsylvania         870770
    Rhode Island          66076
    South Carolina       378959
    South Dakota          63742
    Tennessee            462414
    Texas             1,539,655
    Utah                134,332
    Vermont              44,708
    Virginia            706,539
    Washington          564,864
    West Virginia       150,021
    Wisconsin           381,940
    Wyoming              48,505
    Name: Veterans, 2011-2015, dtype: object



**Observation**: numbers are stored as strings and do not have a consistent format


```python
# replacing commas
df_c_raw['Veterans, 2011-2015'] = df_c_raw['Veterans, 2011-2015'].str.replace(",", "")
```


```python
# converting to numeric type
df_c_raw['Veterans, 2011-2015'] = pd.to_numeric(df_c_raw['Veterans, 2011-2015'], errors='coerce')
```


```python
# check if everything worked
df_c_raw['Veterans, 2011-2015']
```




    Alabama            363170
    Alaska              69323
    Arizona            505794
    Arkansas           220953
    California        1777410
    Colorado           391725
    Connecticut        199331
    Delaware            71213
    Florida           1507738
    Georgia            670617
    Hawaii             110238
    Idaho              119711
    Illinois           668933
    Indiana            426493
    Iowa               211066
    Kansas             198396
    Kentucky           297312
    Louisiana          281989
    Maine              119058
    Maryland           403900
    Massachusetts      355083
    Michigan           626722
    Minnesota          342388
    Mississippi        184774
    Missouri           451342
    Montana             90000
    Nebraska           132918
    Nevada             220332
    New Hampshire      106827
    New Jersey         393277
    New Mexico         164157
    New York           828586
    North Carolina     696119
    North Dakota        51179
    Ohio               806531
    Oklahoma           295847
    Oregon             306723
    Pennsylvania       870770
    Rhode Island        66076
    South Carolina     378959
    South Dakota        63742
    Tennessee          462414
    Texas             1539655
    Utah               134332
    Vermont             44708
    Virginia           706539
    Washington         564864
    West Virginia      150021
    Wisconsin          381940
    Wyoming             48505
    Name: Veterans, 2011-2015, dtype: int64



#### Variable 'Foreign born persons, percent, 2011-2015'


```python
# print out all values
df_c_raw['Foreign born persons, percent, 2011-2015']
```




    Alabama            3.50%
    Alaska             7.40%
    Arizona           13.50%
    Arkansas           4.70%
    California        27.00%
    Colorado           9.80%
    Connecticut       13.90%
    Delaware           8.70%
    Florida           19.70%
    Georgia            9.80%
    Hawaii            17.70%
    Idaho              6.10%
    Illinois          14.00%
    Indiana            4.80%
    Iowa               4.70%
    Kansas             6.90%
    Kentucky           3.40%
    Louisiana          4.00%
    Maine              3.50%
    Maryland          14.50%
    Massachusetts     15.50%
    Michigan           6.30%
    Minnesota          7.70%
    Mississippi        2.30%
    Missouri           3.90%
    Montana            2.10%
    Nebraska           6.60%
    Nevada            19.20%
    New Hampshire      5.70%
    New Jersey        21.70%
    New Mexico         0.098
    New York           0.225
    North Carolina     0.077
    North Dakota       0.032
    Ohio               0.041
    Oklahoma           0.058
    Oregon             0.099
    Pennsylvania       0.063
    Rhode Island       0.133
    South Carolina     0.048
    South Dakota        0.03
    Tennessee          0.048
    Texas             16.60%
    Utah               8.40%
    Vermont            4.30%
    Virginia          11.70%
    Washington        13.40%
    West Virginia      1.50%
    Wisconsin          4.80%
    Wyoming            3.60%
    Name: Foreign born persons, percent, 2011-2015, dtype: object



**Observation**: percentages are stored with the sign (%) and without.


```python
# function to remove '%' and divide by 100
def clean_percentage(x):
    if '%' in x:
        x = x.replace('%', '')
        x = float(x) / 100
        return x
    else:
        return float(x)
```


```python
# applying the function
df_c_raw['Foreign born persons, percent, 2011-2015'] = df_c_raw['Foreign born persons, percent, 2011-2015'].apply(clean_percentage)
```


```python
# convert to numeric type
df_c_raw['Foreign born persons, percent, 2011-2015'] = pd.to_numeric(df_c_raw['Foreign born persons, percent, 2011-2015'], errors='coerce')
```


```python
# resetting the index
df_c_raw = df_c_raw.reset_index()   
```


```python
# check if everything worked
df_c_raw['Foreign born persons, percent, 2011-2015']
```




    0     0.035
    1     0.074
    2     0.135
    3     0.047
    4     0.270
    5     0.098
    6     0.139
    7     0.087
    8     0.197
    9     0.098
    10    0.177
    11    0.061
    12    0.140
    13    0.048
    14    0.047
    15    0.069
    16    0.034
    17    0.040
    18    0.035
    19    0.145
    20    0.155
    21    0.063
    22    0.077
    23    0.023
    24    0.039
    25    0.021
    26    0.066
    27    0.192
    28    0.057
    29    0.217
    30    0.098
    31    0.225
    32    0.077
    33    0.032
    34    0.041
    35    0.058
    36    0.099
    37    0.063
    38    0.133
    39    0.048
    40    0.030
    41    0.048
    42    0.166
    43    0.084
    44    0.043
    45    0.117
    46    0.134
    47    0.015
    48    0.048
    49    0.036
    Name: Foreign born persons, percent, 2011-2015, dtype: float64



### Creating another dataframe with the number of permits from 2011 to 2015


```python
# create a dataframe with the number of permits in 2011 to 2015
permits = (df_gd[df_gd.month.between("2011-01", "2015-12")].groupby("state")["permit"].sum().reset_index())
permits.set_index('state', inplace=True)
```


```python
# create a dataframe with specific facts
df_t = df_c_raw[['index', 'Veterans, 2011-2015', 'Foreign born persons, percent, 2011-2015']]
```


```python
# add the number of permits between 2011 and 2015
df_t = df_t.join(permits['permit'], on='index')
df_t['permit'] = df_t['permit'].astype('int64')
```

<a id='eda'></a>
## Exploratory Data Analysis

<a id='q1'></a>
### Q1: Does the number of veterans per state affect the number of gun purchases?


```python
# create a scatter plot
df_t.plot(x='Veterans, 2011-2015', y='permit', kind='scatter')
plt.ticklabel_format(style='plain')
plt.show()
```


![png](output_38_0.png)


<a id='q2'></a>
### Q2: Does the number of foreign born persons per state affect the number of gun purchases?


```python
# create a scatter plot
df_t.plot(x='Foreign born persons, percent, 2011-2015', y='permit', kind='scatter')
plt.ticklabel_format(style='plain')
plt.show()
```


![png](output_40_0.png)


<a id='q3'></a>
### Q3: What is the overall trend of gun purchases?


```python
# preparing the dataframe

# setting the index to 'month'
df_gd.index = df_gd.month
```


```python
# group by state
# using resample to calculate sums per year
# turning the series into a dataframe
# source: https://stackoverflow.com/questions/32012012/pandas-resample-timeseries-with-groupby
df_sum = df_gd.groupby('state').resample('A')['permit'].sum().to_frame()
```


```python
# keeping the ticklabel_format as in the dataframe
plt.ticklabel_format(style='plain')
# group by month and calculate sum to see the overall development
df_sum.groupby('month')['permit'].sum().plot()
plt.show()
```


![png](output_44_0.png)



```python
df_sum.groupby('month').sum()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>permit</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1998-12-31</th>
      <td>78169.0</td>
    </tr>
    <tr>
      <th>1999-12-31</th>
      <td>1037700.0</td>
    </tr>
    <tr>
      <th>2000-12-31</th>
      <td>1227814.0</td>
    </tr>
    <tr>
      <th>2001-12-31</th>
      <td>1408338.0</td>
    </tr>
    <tr>
      <th>2002-12-31</th>
      <td>1363211.0</td>
    </tr>
    <tr>
      <th>2003-12-31</th>
      <td>1403496.0</td>
    </tr>
    <tr>
      <th>2004-12-31</th>
      <td>1345672.0</td>
    </tr>
    <tr>
      <th>2005-12-31</th>
      <td>1350193.0</td>
    </tr>
    <tr>
      <th>2006-12-31</th>
      <td>2037453.0</td>
    </tr>
    <tr>
      <th>2007-12-31</th>
      <td>3078802.0</td>
    </tr>
    <tr>
      <th>2008-12-31</th>
      <td>3699021.0</td>
    </tr>
    <tr>
      <th>2009-12-31</th>
      <td>4450822.0</td>
    </tr>
    <tr>
      <th>2010-12-31</th>
      <td>4884307.0</td>
    </tr>
    <tr>
      <th>2011-12-31</th>
      <td>5545457.0</td>
    </tr>
    <tr>
      <th>2012-12-31</th>
      <td>5683547.0</td>
    </tr>
    <tr>
      <th>2013-12-31</th>
      <td>6169832.0</td>
    </tr>
    <tr>
      <th>2014-12-31</th>
      <td>7769858.0</td>
    </tr>
    <tr>
      <th>2015-12-31</th>
      <td>8782048.0</td>
    </tr>
    <tr>
      <th>2016-12-31</th>
      <td>11134651.0</td>
    </tr>
    <tr>
      <th>2017-12-31</th>
      <td>7469845.0</td>
    </tr>
  </tbody>
</table>
</div>



<a id='conclusions'></a>
## Conclusions

### Does the number of veterans per state affect the number of gun purchases?

The scatter plot shows that the amount of veterans in a state does not have an effect on the number of gun permits. You cannot state that a high/low number of veterans lead to a high/low number of gun permits.

### Does the number of foreign born persons per state affect the number of gun purchases?

The same observations applies for the variable "foreign born persons": there seems to be no connection between a high/low percentage of these individuals with the number of gun permits.

### What is the overall trend of gun purchases?

The overall trend of gun purchases (permits to be precise) shows a steady increase beginning in 2005. The maximum is reached in 2016 with over 11 million permits. There is a noticable drop in 2017 where the number of permits is on the same level as in 2014.


```python
from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])
```




    0


