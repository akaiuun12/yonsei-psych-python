# week5.py

# BASIC LIBRARIES
import os

# DATA PROCESSING LIBRARIES
import pandas as pd
import scipy.stats as stats


# LOAD DATA
files = os.listdir('data')
data = pd.DataFrame()

for file in files:
    tmp_data = pd.read_csv(f'data/{file}')
    tmp_data = tmp_data.dropna()
    tmp_data['trl'] = range(len(tmp_data))
    tmp_data['zscore'] = stats.zscore(tmp_data['rt'])
    data = pd.concat([data, tmp_data])

data = data[data['zscore'].between(-2,2)]
data.groupby('sn').describe()


# DATA VISUALIZATION LIBRARIES
import matplotlib.pyplot as plt
import seaborn as sns

# HISTOGRAM
sns.histplot(
    data=data,
    x='rt',
    hue='sn',
    kde=True
)
plt.show()


# SIMPLE LINEPLOT WITH TITLE
sns.lineplot(
    data=data,
    x='trl', 
    y='rt',
    hue='sn'
)
plt.title('RT variation by trials')
plt.xlabel('Trials')
plt.ylabel('Response Time (ms)')
plt.show()


# SAVING BARPLOT WITH LIMITED Y-AXIS
sns.barplot(
    data=data,
    x='sn',
    y='cor'
)
plt.title('Barplot by Participants')
plt.xlabel('Subject Number')
plt.ylabel('Accuracy (%)')
plt.ylim([0.8, 1.0])

plt.savefig('data/fig3.png')
plt.show()


# SCATTERPLOT WITH OPACITY
sns.set_style('darkgrid')
sns.scatterplot(
    data=data,
    x='trl',
    y='rt',
    hue='sn',
    alpha=0.7
)
plt.savefig('data/fig4.png', dpi=300)
plt.show()


# STATISTICAL ANALYSIS LIBRARIES
import scipy as sp
import scipy.stats as stats

# USING SCIPY
data1 = data[data['sn']==1]
data2 = data[data['sn']==2]

result1 = stats.ttest_1samp(data['rt'], popmean=0)
result2 = stats.ttest_ind(data1['rt'], data2['rt'].dropna())

print(result1)
print(result2)


import statsmodels.api as sm
import statsmodels.formula.api as smf

# USING STATSMODELS
model = smf.ols(
    data=data, 
    formula='rt ~ cor*sn'
)
result = model.fit()
help(result)
print(result.summary())