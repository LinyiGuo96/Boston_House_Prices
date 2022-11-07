# -*- coding: utf-8 -*-

#%% Import pkgs

import pandas as pd
import numpy as np
pd.options.display.max_rows = 90
pd.options.display.max_columns = 90

import os


#%% Load raw data

if os.getcwd() == 'E:\GitHubRepo':
    os.chdir('Boston_House_Prices')
elif os.getcwd() == 'E:\GitHubRepo\Boston_House_Prices':
    pass
    
      
      
train0 = pd.read_csv("data/train.csv")
test0 = pd.read_csv("data/test.csv")
sample_submission = pd.read_csv("data/sample_submission.csv")

print(train0.head())
print('Data load successfully!')

#%% Combine Train and Test Sets

target = train0['SalePrice']
test_ID = test0['Id']

train1 = train0.drop(['Id', 'SalePrice'], axis = 1)
test1 = test0.drop('Id', axis = 1)

data1 = pd.concat([train1, test1], axis = 0).reset_index(drop=True)

print(data1)
print(target)

print('----------------------\n Combine done \n----------------------')

#%% Cleaning - Ensure proper data type
data2 = data1.copy()
print(data2.head())

print(data2.dtypes)

data2['MSSubClass'] = data2['MSSubClass'].astype('str')

print('----------------------\n Change type Done \n----------------------')

#%% Cleaning - Missing Values

data2.isnull().sum()

data2.



#%% 



#%%
#%%
#%%
#%%
#%%
#%%
#%%
 