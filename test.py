import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
pd.options.display.width
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoption(linewidth=desired_width)
pd.set_option('display.max_columns',10)

# change the work directory
os.getcwd()
os.chdir("E:\GitHubRepo\Boston_House_Prices")

# read the training set
train_data = pd.read_csv("data/train.csv")

train_data.head()

train_data.describe()

# Data Explore by plotting

plt.plot(train_data['LotArea'], train_data['SalePrice'])

