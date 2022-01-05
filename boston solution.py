# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:27:07 2021

@author: Oluwajuwon
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

boston = pd.read_csv('Boston.csv')
boston = boston.drop(columns = ['Unnamed: 0'])

pair = sns.pairplot(boston)
plt.savefig('boston pairplot')

plt.figure(figsize = (20,18))
boston_corr = sns.heatmap(boston.corr().round(2), annot = True)
plt.savefig('boston_corr')

plt.scatter(x = boston['lstat'], y = boston['crim'])

sns.pairplot(data = boston, vars = ['crim', 'age', 'dis','rad', 'tax', 'ptratio'])
plt.savefig('crim_pair')


boston.corrwith(boston['crim'])

list(boston)


# d
sns.histplot(boston['crim'])
boston['crim'].sort_values(ascending = False).head(10)

sns.histplot(boston['tax'], bins = 25)
boston['tax'].sort_values(ascending = False)

boston['tax'][boston['tax'] > 500]

sns.histplot(boston['ptratio'], bins = 25)

# e
boston['chas'].value_counts()

# f
boston['ptratio'].median()

# g
boston.median()
boston.columns[boston.median() == 0]
boston.columns[boston.median().min()]  ### sematic error

boston.median().min()

boston['medv'][boston['medv'].min()]
boston.index(min(boston['medv']))

boston['medv'].idxmin()
m = boston[boston['medv'] == boston['medv'].min()]
m.min()
# h
