def inf():
    print('数据达人培养计划，模块练习')

def power(a):
    y=a**2
    return y

#阶层函数f1(n)
def f1(n):
    y=1
    for i in range(1,n+1):
        y*=i
    return y
    
#列表删值函数f2(lst,x)
def f2(lst,x):
    for i in lst:
        if i==x:
            lst.remove(i)
    return lst

#等差数列求和函数f3(a,d,n)
def f3(a,d,n):
    s=0
    for i in range(1,n+1):
        s=s+a
        a=a+d
    return s
        
