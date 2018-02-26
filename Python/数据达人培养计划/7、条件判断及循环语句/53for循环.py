'''
n=int(input('输出次数：'))
for i in range(n):
    print(i,"hello world")
'''
'''
#等差数列求和
a=float(input('首项：'))
n=int(input('项数：'))
d=float(input('公差：'))
s=0

for i in range(n):
    s=s+a
    a=a+d
print(s)
'''
'''
#组合字典
k=['a','b','c']
v=[1,2,3]

m=[]

for i in range(len(k)):
    m.append([k[i],v[i]])
    m2=dict(m)
print(m2)
'''

#for循环做阶层运算：n!
n=int(input('阶层运算n='))
m=1

for i in range(1,n+1):
    m=m*i
print(m)


