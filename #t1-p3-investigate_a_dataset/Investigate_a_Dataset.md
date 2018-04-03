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

Observations:
- The column 'month' has an incorrect datatype (_object_ instead of _datetime64[ns]_)

### General Properties of the file: U.S. Census Data.csv

Getting a general overview over the data:

```python
df_c_raw.info()
```

Observations:
- The column 'Fact Note' can be dropped.
- The last 20 rows of the file contain explanations and can be dropped.
- The columns and rows are switched (rows contain variables and the columns contain the states).


### Data Cleaning (gun_data.xlsx)

```python
# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.

```

### Data Cleaning (U.S. Census Data.csv)

```python
# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.

```

<a id='eda'></a>
## Exploratory Data Analysis

> **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.

### Is a high number of veterans per state associated with a high number of guns (and vice versa)?


```python
# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.

```

### Is a high number of foreign born persons per state associated with a high number of guns (and vice versa)?


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
