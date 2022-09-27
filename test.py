# Import packages

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import warnings


pd.options.display.width
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoption(linewidth=desired_width)
pd.set_option('display.max_columns',10)

# change the work directory
os.getcwd()
os.chdir("E://GitHubRepo/Boston_House_Prices")
print(os.listdir("data")) # list files in data folder
warnings.filterwarnings('ignore')

# read the training set
train_data = pd.read_csv("data/train.csv")

train_data.head()

train_data.describe()

# Data Explore by plotting

'''this part is replaced by Power BI.'''




