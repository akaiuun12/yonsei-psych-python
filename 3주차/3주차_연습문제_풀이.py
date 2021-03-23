# 3주차_연습문제_풀이.py

# 함수의 입력값이 정해지지 않았을 경우 어떻게 할까? 임의의 숫자를 입력하면 해당 숫자를 모두 더하는 함수를 만들어보자.
def summation(*arg):
    result = sum(arg)
    print(type(arg))
    return result

summation(1,2,3)

# 특정 폴더의 파일명을 모두 불러와보자. 그 뒤 해당 폴더의 파일명을 숫자로 바꿔보자.

files = os.listdir('sample')

for i, file in enumerate(files): 
    print(file)
    os.rename(f'sample/{file}', f'sample/{i}.py')

# random을 사용해서 특정 범위의 숫자나 특정 리스트의 요소를 뽑아보자. 복원 추출인가 아니면 비복원 추출인가? 복원 추출 혹은 비복원 추출을 지정하려면 어떻게 해야하는가?

import random
stimuli = ['a', 'b', 'c']

# 복원 추출
for i in range(len(stimuli)):
    print(random.choice(stimuli))

# 비복원 추출
random.shuffle(stimuli)

for i in range(len(stimuli)):
    print(stimuli.pop())