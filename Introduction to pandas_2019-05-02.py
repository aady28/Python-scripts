# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:46:37 2019

@author: RatwanaS
"""

#Introduction to Pandas

#Pandas is an open source pyhton library 
#Provides:
   # 1. easy to use data structures
   # 2. data analysis tools
   # runs on top of numpy
   
#Difference btw numpy and pandas
   #numpy: low level data structure (np.array)
   #supports large multi dimantional arrays and matrices
   #range of mathematical array operations 
   #pandas: high level  data structure (data  frames)
   #streamlined data in a tabular form
   #time series functionality
   #data alignment, missing data analysis, groupby, join, merge methods
   #pandas data structures can be used along with numpy and other functions to manipulate them


import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[0, 1, 2, 3])    
print(df1)

path="C:/Users/RATWANAS/Desktop/Coding & Automation/Datasets/Data for training/"

# Note that pd.read_csv is used because we imported pandas as pd
surveys_df =pd.read_csv(path+"surveys.csv")

import sklearn
from sklearn import datasets
d = datasets.load_iris()
surveys_df = d.data
d1 = pd.DataFrame(surveys_df)
surveys_df = d1
surveys_df.colnames = ['A','B','C','D']

surveys_df.head() # The head() method displays the first several lines of a file
                  
type(surveys_df)
surveys_df.dtypes 
#by column names

surveys_df.columns
pd.unique(surveys_df['species_id'])

site_names=pd.unique(surveys_df['weight'])
len(site_names)
surveys_df['species_id'].nunique() #NULL not counted

#We can calculate basic statistics for all records in a single column using the syntax below:
summary=surveys_df.describe()
perc =[.20, .40, .60, .80]
include =['object', 'float', 'int']
surveys_df.describe(percentiles= perc)
#include= ['O']
#We can calculate basic statistics for all records in a single column using the syntax below:
all_summary=surveys_df.describe(include=[np.object])
length = pd.DataFrame({'species_id': [len(surveys_df['species_id'])],'sex': [len(surveys_df['species_id'])]},index=["total count"])
all_summary1=length.append(all_summary)

surveys_df['sex'].value_counts()

len(surveys_df[(surveys_df['species_id'].isin(["SH"]))]['species_id']) # not in
#Selecting data using Labels (Column Headings)
# Method 1: select a 'subset' of the data using the column name
surveys_df['species_id']

# Method 2: use the column name as an 'attribute'; gives the same output
surveys_df.species_id

# Creates an object, surveys_species, that only contains the `species_id` column
surveys_species = surveys_df['species_id']
#We can pass a list of column names too, as an index to select columns in that order. 
#This is useful when we need to reorganize our data.

# Select the species and plot columns from the DataFrame
surveys_df[['species_id', 'plot_id']]
surveys_df[['plot_id', 'species_id']]

# Select rows 0, 1, 2 (row 3 is not selected)
surveys_df[0:3]
"""
We can select specific ranges of our data in both the row and column directions using either label 
or integer-based indexing.

loc is primarily label based indexing. Integers may be used but they are interpreted as a label.
iloc is primarily integer based indexing
"""

surveys_df=surveys_df.set_index('species_id')
surveys_df[:1]
surveys_df.iloc[0:3]
surveys_df.iloc[0:3,[1,2]+list(range(2,5))]

surveys_df.loc['DM',:]


surveys_df=surveys_df.reset_index()
surveys_df[0:3]
# Select the first 5 rows (rows 0, 1, 2, 3, 4)
surveys_df[:5]

# Select the last element in the list
# (the slice starts at the last element, and ends at the end of the list)
surveys_df[-1:]
# Assign the value `0` to the first three rows of data in the DataFrame
ref_surveys_df = surveys_df
ref_surveys_df[0:3] = 0
              
# ref_surveys_df was created using the '=' operator
ref_surveys_df.head(3)

# surveys_df is the original dataframe
surveys_df.head()


surveys_df =pd.read_csv(path+"surveys.csv")

#surveys_df=surveys_df.set_index('weight')
# ilocandloc[row slicing, column slicing]
surveys_df.iloc[0:3, 1:4]
surveys_df.loc[0:3, 1:4]

# Select all columns for rows of index values 0 and 10
surveys_df.loc[[0, 10]]

# What does this do?
surveys_df.loc[0, ['species_id', 'plot_id', 'weight']]

# What happens when you type the code below?
surveys_df.loc[[0, 10, 35549], :]

surveys_df.loc[[1, 10], :]
surveys_df.iloc[[1, 10], 1:4]

surveys_df.iloc[2, 6]

surveys_df=surveys_df.reset_index()
#surveys_df=surveys_df.set_index('weight')
surveys_df[0:1]
surveys_df[:4]
surveys_df[:-1]

surveys_df.iloc[0:4, 1:4]
surveys_df.loc[:-1,]

#Subsetting Data using Criteria

surveys_df[surveys_df.year == 2002]
surveys_df[surveys_df.year != 2002]
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]

surveys_df[(surveys_df.year == 1999) &(surveys_df.weight<=8)]
surveys_df[surveys_df['species_id'].isin(['DM'])] #  %in%
surveys_df[~(surveys_df['species_id'].isin(["DM","SH"]))] # not in
