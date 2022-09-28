import pandas as pd
import os

os.getcwd()
os.chdir('Boston_House_Prices')

input = pd.read_csv('data/train.csv')

input.head()

input.describe()

input.shape # (1460, 81)

input.value_counts()

input.dtypes

input = input.dropna()

input.shape