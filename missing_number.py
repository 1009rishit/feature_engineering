# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcDRaj9hUZONAwtOy1p0SyWO0bfgNjaS
"""

import seaborn as sns
import pandas as pd
import numpy as np

df=sns.load_dataset("titanic")

df.head()

df.isnull().sum() #no. of missing values

df.isnull().mean()

df.shape

new_df=df.dropna() #row wise deletion

new_df.shape

"""#mean_value imputation"""

sns.distplot(df['age'])

df['age_mean']=df['age'].fillna(df['age'].mean())

df[['age_mean','age']]

"""#this technique work well when your data is normally distributed

**2-MEDIAN VALUE IMPUTATION**
"""

df['age_median']=df['age'].fillna(df['age'].median())

df[['age_median','age_mean','age']]



"""**3-MODE VALUE IMPUTATION**"""

df[df['embarked'].isnull()]

df['embarked'].unique()

mode=df[df['age'].notna()]['embarked'].mode()[0]

mode

df['embarked_mode']=df['embarked'].fillna(mode)

df[['embarked_mode']]

df['embarked_mode'].isnull().sum()

