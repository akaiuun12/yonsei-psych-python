# prac.py

import pandas as pd

# 민트 초코에 대한 10명의 선호도 (10점 만점)
Mincho = [
    9.5, 
    5.6, 
    7.8, 
    6.1, 
    4.9, 
    7.0, 
    6.5, 
    5.8, 
    6.2, 
    6.8]
data = pd.DataFrame(Mincho)

data = pd.read_csv('pandas_practice.csv')
# data = pd.read_csv('파일 경로', delimiter='\t')
# data = pd.read_csv('파일 경로', header=None)

data
data.shape
data.head(n=10)
data.tail(n=10)
data.columns

data.mean()  # 0    6.62
data.sum()   # 0    66.2
data.var()   # 0    1.666222
data.std()   # 0    1.290822

data.describe()

data.isna()
replaced_data = data.fillna(0)
dropped_data = data.dropna(
    axis='rows', # 옵션: 'rows', 'columns'
    how='any' # 옵션: 'any', 'all'
)
data

dropped_data = dropped_data.reset_index()
dropped_data

dropped_data['rt'][3:5]

dropped_data['rt']
dropped_data.loc[:,'rt']

dropped_data['rt'][3:5]
dropped_data.iloc[3:5, 2]





# import random
# import numpy as np
# import scipy as sp
# import scipy.stats as stats

# data2 = pd.DataFrame()
# data

# data2['sn'] = np.repeat(2, len(data))
# zeros = np.zeros(15)
# ones = np.ones(len(data) - len(zeros))

# zeros.shape
# ones.shape
# corr = np.concatenate([zeros, ones])
# random.shuffle(corr)

# data2['cor'] = corr

# rt2 = population.rvs(size=len(data))
# data2['rt'] = np.abs(data['rt'] + rt2)

# data2.describe()

# data2.to_csv(
#     'pandas_practice2.csv', 
#     index=False
#     )

# data2 = pd.read_csv('pandas_practice2.csv')
# data2.shape
# data2

data = pd.concat([data, data2])
data.describe()
data.groupby('sn').describe()

data
data.dropna()

dropped_data['rt'] * 1000

dropped_data
dropped_data.iloc[3, 2]
dropped_data['rt'][3:5]



dropped_data.describe()

data.describe()