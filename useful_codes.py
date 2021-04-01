# settings.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# numpy 화면 출력 표기법을 설정한다.
np.set_printoptions(suppress=True,
	formatter={'float_kind':'{:.1f}'.format})

# matplotlib 스타일을 설정해준다.
plt.style.use('tableau-colorblind10')
# plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-colorblind')
# plt.style.use('seaborn-dark')

# matplotlib 전역 한글 출력을 설정한다. 
from matplotlib import rc
# rc('font', family='AppleGothic') # for Mac OSX
rc('font', family='Noto Sans KR') # for Windows

# 마이너스 부호 표시
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# pandas 화면에 출력되는 행, 열의 개수를 조절한다. None은 무제한
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)