import pandas as pd
import os

os.getcwd()
os.chdir('Boston_House_Prices')

input = pd.read_csv('data/train.csv')

input.head()

pd.options.display.width
pd.set_option('display.width', 300)
pd.set_option('display.max_columns',10)

input.head()

input.describe()

input.shape # (1460, 81)

input.value_counts()

dtypes = input.dtypes
del(dtypes)

input_shuffled = input.sample(n=len(input), random_state=1)

input_shuffled

pd.get_dummies(input_shuffled['MSZoning']).head()


# split train & test data

from sklearn.model_selection import train_test_split

train, test = train_test_split(input_shuffled, test_size=0.3)

X_train, y_train = train.to_numpy()[:, :-1], train.to_numpy()[:, -1]
X_test, y_test = test.to_numpy()[:, :-1], test.to_numpy()[:, -1]

X_train.shape # (1022, 80)
X_test.shape # (438, 80)















