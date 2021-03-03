# week3.py

import os

os.getcwd() # 현재 작업경로
os.chdir()


os.chdir('C:/Users') 
os.getcwd()

os.chdir('../') # 작업경로 변경
os.chdir('C:/Users/Red/Documents/GitHub/yonsei-psych-python/3주차') # 
os.getcwd()


files = os.listdir() # 입력이 없으면 현재 위치

print(files)


def repeat(string):
    result = str(string) * 2
    return result

repeat(2)
repeat('apple')


def introduce():
    print('Hello World!')

introduce()

def sum_diff(a, b):
    result1 = a + b
    result2 = a - b
    return result1, result2

sum_diff(10,2)

def sum_diff(a, b):
    summation = a + b
    difference = a - b
    return summation, difference

result1, result2 = sum_diff(10,2) # (12, 8)

print(result1)
print(result2)


def sum_diff(a, b):
    summation = a + b
    difference = a - b
    return summation, difference

result = sum_diff(10, 2)
result1, result2 = sum_diff(10, 2) # (12, 8)

print(result1)
print(result2)

print(result[0])
print(result[1])

def introduce(lang='Python'):
    return f'{lang} is Fun!'

introduce()
introduce('Javascript')


beatles = ['Harrison', 'Lennon', 'Starr', 'McCartney']

print(len(beatles))

pi = 3.1415926535897932384
round(pi, 2)

pi = 3.1415926535897932384
round(pi, 2)    # 3.14
round(pi, 5)    # 3.14159

os.getcwd()
os.chdir('./3주차')

import random

random.randint(1, 10)
random.randrange(10,20)

beatles = ['Harrison', 'Lennon', 'Starr', 'McCartney']

favorite = random.choice(beatles)
print(favorite)

beatles

greek = ['alpha', 'beta', 'gamma']

random.shuffle(greek)

print(greek)

import sample

sample.liers('Life is short')

from sample import truthtellers
truthtellers('You need Python')


from sample import truthtellers
truthtellers('You need Python')
liers('You need Python')