# 2주차_제어문.py

a = 10
b = 5
c = 0
d = 1

a > b       # Greater than
a == b      # Equal to
a < b       # Less than
c != True   # Not Equal to

print(a > b)        # True
print(a == b)       # False
print(a < b)        # False
print(c != True)    # True


RT = 600

if RT < 250:
    print('Too Fast!')
else:
    print("It's Okay")
elif RT > 500:
    print('Too Slow!')

# Too Slow!

scientist = ['einstein', 'maxwell', 'newton']


scientist = tuple(scientist)

'einstein' in scientist         # True
type('einstein' in scientist)   # bool

'shakespeare' in scientist      # False

a = [0,1,2,3,4,5,6,7,8,9]

for number in a:
    print(number)

for number in range(10):
    print(number)

e = 3
e = e+1
e = e+100

print(e)

e = 3
e += 1      # 4
e += 100    # 104

print(e)

