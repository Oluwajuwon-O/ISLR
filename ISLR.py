# (a)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# (b)
college = pd.read_csv('College.csv')
college = college.rename(columns = {'Unnamed: 0':'School'})
college = college.set_index('School')

# (c)

# i. 
summary = pd.DataFrame(college.describe())
print(summary)

# ii. 
col = college.iloc[:,0:10]
sns.pairplot(col)

# iii.
# Outstate vs Private
sns.boxplot(data = college, x = 'Private', y = 'Outstate')

# iv. 
temp = []
for i in college['Top10perc']:
    if i > 50:
        temp.append('Yes')
    else:
        temp.append('No')
college['Elite'] = temp

college[['Elite']].value_counts()

# 9. 
auto = pd.read_csv('Auto.csv')
auto.isnull().sum()
auto.info()

# b.
print('range of quantitative predictors')
quantitative =  auto.select_dtypes(include = ['float64'])
print(quantitative)
print(quantitative.max() - quantitative.min())

# c. 
print('mean & std of  quantitative predictors')
print('mean')
print(quantitative.mean())
print('')
print('standard deviation')
print(quantitative.std())


# d. 
# need = quantitative.drop(index = [[10:86]])
need = quantitative.drop(quantitative.index[10:86])
print('range')
print(need.max()-need.min())
print('')
print('mean')
print(need.mean())
print('')
print('standard deviation')
print(need.std())

list(auto)
auto_corr = auto.corr().round(3)
print(auto_corr)

auto_hm = sns.heatmap(auto_corr, annot = True)

sns.pairplot(auto)
