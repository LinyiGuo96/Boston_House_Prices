# Preface

This file is to save my notes/ideas while learning and exploring. 

# Body

**Change the directory of Jupyter Notebook**

```{python}
jupyter notebook --notebook-dir C:/users/lincoln
```

**delete objects**

`del` 


- Cleaning
- Feature engineering
- Feature transformations
- Feature selection
- Encoding
- Scaling
- Target transformation
- Model selection
- Hyperparameter optimization
- Ensembling


`train.isna().sum()`

`pd.concat([table1, table2], axis = 0).reset_index(drop=True)` 

`table.select_dtypes(np.number)`

`data1 = data.copy()`

`np.log1p()`: log(x+1)

log transformation: skewed data

sin()/cos() transformation: for months, cause months are like a cycle, that is, Dec (12) should be next to Jan (1), otherwise models will think 12 (Dec) is greater than 1 (Jan)

![img.png](img.png)


## **pycaret** library

`!pip install -q pycaret`

**Model selection**

`from pycaret.regression import setup, compare_models`

 
**Bagging Ensemble**

I have learned(heard) about bagging(ensembling) before, the idea is to use several model in parallel to prediction. But I haven't seen anyone use this method in practice, it's a good chance to learn it by this exercise.

Add weights to different models -> **Question: A better way to determine the weights?**

## Feature Engineering

This means we can create some new features by using the existing features. For example, use the total price of a house divided by the lot area, to get the unit price.


## Hyperparameter Optimization

[Optuna](https://optuna.org/)





