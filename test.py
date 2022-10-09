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
