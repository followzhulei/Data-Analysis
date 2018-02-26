'''
import mo

print(mo.f1(5))
print(mo.f2([1,2,3,4],3))
print(mo.f3(1,2,3))
'''
#random模块
'''
import random

x=random.random()
y=random.random()

m=random.randint(5,50)
print(m)

st=random.choice([1,2,3,4,5,7])
st2=random.choice('adfsfaegag')
print(st,st2)

lst=list(range(10))
sli=random.sample(lst,5)
print(lst,sli)

str1=['a','b','c','d','e','f','g']
random.shuffle(str1)
print(str1)
'''

#time模块

import time

print(time.ctime())
print(type(time.ctime()))
print(time.localtime())

print(time.strftime('%Y-%m-%d %H:%M:%S %w',time.localtime()))

























