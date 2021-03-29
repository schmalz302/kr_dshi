import os
from random import choice

os.listdir()
a = {}
b = []
for i in os.listdir('художники'):
    a[i] = []
    b.append(i)
    for j in os.listdir(f'художники/{i}'):
        a[i].append(j)
x = choice(b)
y = choice(a[x])
print(f'{x}/{y}')