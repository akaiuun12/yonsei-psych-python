# week4.py
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


## pd.read_csv(): csv 파일 불러오기
data = pd.read_csv('pandas_practice.csv')
data = pd.read_csv('파일 경로', delimiter='\t')
data = pd.read_csv('파일 경로', header=None)


# 만든 데이터프레임을 직접 살펴봅시다.
data


data.mean()  # 0    6.62
data.sum()   # 0    66.2
data.var()   # 0    1.666222
data.std()   # 0    1.290822

## df.describe: 요약 통계량
help(data.describe())

## df.shape: 데이터의 크기 확인하기
data.shape) # (360, 3

data.head(n=5)
data.tail(n=5)

data.columns[0]

# 결측값 및 이상값 처리

data.isna()

#         sn    cor     rt
# 0    False  False  False
# 1    False  False  False
# 2    False  False  False
# 3    False  False  False
# 4    False  False   True
# ..     ...    ...    ...
# 355  False  False  False
# 356  False  False  False
# 357  False  False  False
# 358  False  False  False
# 359  False  False  False

# [360 rows x 3 columns]

data.isna().sum()

# sn      0
# cor     0
# rt     10
# dtype: int64

## df.fillna(): 결측치를 다른 값으로 대체
filledData = data.fillna(0)
cleanData = data.dropna(
    axis='rows', # 옵션: 'rows', 'columns'
    how='any' # 옵션: 'any', 'all'
)

cleanData.shape
filledData.head()
cleanData.head()

## df['새로운 열 이름'] = data
cleanData['age'] = 22
cleanData['age'] # Broadcast

cleanData.head()

# iloc
# : integer position을 통해 값을 찾는다.
# ​
# loc
# : label을 통해서 값을 찾는다.
# ​

cleanData.loc[5]
cleanData.iloc[5]

#    sn  cor     rt  age
# 0   1    0  0.634   22
# 1   1    1  0.356   22
# 2   1    1  0.337   22
# 3   1    1  0.386   22
# 5   1    1  0.287   22
```


## df.rename(columns={prev:new})
```python
cleanData = cleanData.rename(
    columns={'sbj':'participant'}
    )

cleanData.head()

#     participant  cor     rt  age
# 0            1    0  0.634   22
# 1            1    1  0.356   22
# 2            1    1  0.337   22
# 3            1    1  0.386   22
# 5            1    1  0.287   22
```


## df.between()
```python
zdata = cleanData[cleanData['zscore'].between(-2,2)]

zdata.shape) # (341, 6
```