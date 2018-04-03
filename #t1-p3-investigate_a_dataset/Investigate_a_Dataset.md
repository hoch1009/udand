# Project: Investigating FBI Gun Data

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
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
%matplotlib inline
```

```python
# Create a dataframe based on the gun_data.xlsx
df_gd = pd.read_excel('gun_data.xlsx')

# Create a dataframe based on the raw census data
df_c_raw = pd.read_csv('U.S. Census Data.csv')

```

<a id='wrangling'></a>
## Data Wrangling

> **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.

### General Properties of the file: gun_data.xlsx

Getting a general overview over the data:

```python
df_gd.info()
```

**Observations:**
- The column 'month' has an incorrect datatype (_object_ instead of _datetime64[ns]_)

### General Properties of the file: U.S. Census Data.csv

Getting a general overview over the data:

```python
df_c_raw.info()
```

**Observations:**
- The column 'Fact Note' can be dropped.
- The last 20 rows of the file contain explanations and can be dropped.
- The columns and rows are switched (rows contain variables and the columns contain the states).


### Data Cleaning (gun_data.xlsx)

```python
# change dtype of the column 'month'
df_gd['month'] = df_gd['month'].astype('datetime64[ns]')
```

### Data Cleaning (U.S. Census Data.csv)

```python
# create dataframe and skip last 20 lines
df_c_raw = pd.read_csv('U.S. Census Data.csv', skipfooter=20, header=0, engine='python')

# drop 'Fact Note' column
df_c_raw = df_c_raw.drop('Fact Note', axis=1)

# setting the index to use "Fact" as keys
df_c_raw.set_index('Fact', inplace=True)

# transpose the dataframe for easier handling
df_c_raw = df_c_raw.transpose()

# get info about the new dataframe
df_c_raw.info()

```

I choose to investigate the variables 'Veterans, 2011-2015' and 'Foreign born persons, percent, 2011-2015' further.

#### Variable 'Veterans, 2011-2015'

```python
# print out all values
df_c_raw['Veterans, 2011-2015']
```
Observation: numbers are stored as strings and do not have a consistent format

```python
# replacing commas
df_c_raw['Veterans, 2011-2015'] = df_c_raw['Veterans, 2011-2015'].str.replace(",", "")
# converting to numeric type
df_c_raw['Veterans, 2011-2015'] = pd.to_numeric(df_c_raw['Veterans, 2011-2015'], errors='coerce')
```

#### Variable 'Foreign born persons, percent, 2011-2015'
```python
df_c_raw['Foreign born persons, percent, 2011-2015']
```
Observation: percentages are stored with the sign (%) and without.

```python
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


# resetting the index
df_c_raw = df_c_raw.reset_index()        

```

<a id='eda'></a>
## Exploratory Data Analysis

> **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.

### Q1: Does the number of veterans per state affect the number of gun purchases?

```python
# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.

```

### Q2: Does the number of foreign born persons per state affect the number of gun purchases?

```python
# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.

```

### Q3: What is the overall trend of gun purchases?

```python
# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.

```

<a id='conclusions'></a>
## Conclusions

> **Tip**: Finally, summarize your findings and the results that have been performed. Make sure that you are clear with regards to the limitations of your exploration. If you haven't done any statistical tests, do not imply any statistical conclusions. And make sure you avoid implying causation from correlation!

> **Tip**: Once you are satisfied with your work, you should save a copy of the report in HTML or PDF form. Before exporting your report, check over it to make sure that the flow of the report is complete. You should probably remove all of the "Tip" quotes like this one so that the presentation is as tidy as possible. It's also a good idea to look over the project rubric, found on the project submission page at the end of the lesson.

> To export the report to the workspace, you should run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the jupyter icon in the upper left). Alternatively, you can download the html report via the **File** > **Download as** submenu and then manually upload it to the workspace directory. Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right. Congratulations!


```python
from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])
```
