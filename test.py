# Import packages

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import warnings


# set up pandas print-out option
pd.options.display.width
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

# change the work directory
os.getcwd()
os.chdir("E://GitHubRepo/Boston_House_Prices")
print(os.listdir("data")) # list files in data folder
warnings.filterwarnings('ignore')



#################################
########    Load Data    ########
#################################

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

train.head()
test.head()

train.describe()
test.describe()

train.shape
test.shape



# Data Explore

'''this plotting part is replaced by Power BI.'''



a = 123
b = a
print(b)


## validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.model_selection import cross_val_score

list = [1,2,3,4,5]
d = {}
for x, y in enumerate(list):
    d[y] = x
print(d)
d.values()


def twoSum(nums):
    # d = {}
    # for x, y in enumerate(nums):
    #     if target - y in d:
    #         return [d[target-y], x]
    #     else:
    #         d[y] = x
    d = {}
    for x, y in enumerate(nums):
        if target - y in d:
            return [d[target-y], x]
        else:
            d[y] = x


x = [1,2,3,4,5]
sum(x)


s = 'LCXXI'
x = [d[i] for i in s]
d = {
    'I':             1,
    'V':             5,
    'X':             10,
    'L':             50,
    'C':             100,
    'D':             500,
    'M':             1000
}

x = [d[i] for i in list(s)]

list(s)

for i in range(len(x)):
    print(i)

#%%
