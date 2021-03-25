# matplotlib.py

# DATA PROCESSING LIBRARIES
import numpy as np
import pandas as pd

# DATA VISUALIZATION LIBRARIES
import matplotlib.pyplot as plt
import seaborn as sns

# STATISTICAL ANALYSIS LIBRARIES
import scipy as sp
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf 

# LOAD DATA
data1 = pd.read_csv('pandas_practice.csv')
data1['trl'] = range(len(data))

data2 = pd.read_csv('pandas_practice2.csv')
data2['trl'] = range(len(data))

data = pd.concat([data1, data2])
data.groupby('sn').describe()

# HISTOGRAM
sns.histplot(
    data=data,
    x='rt',
    hue='sn',
    kde=True
)
plt.show()

# SIMPLE LINEPLOT
sns.lineplot(
    data=data,
    x='trl', 
    y='rt'
)
plt.show()

# BARPLOT WITH TITLE
sns.barplot(
    data=data,
    y='rt'
)
plt.show()

