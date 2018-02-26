#函数，完成某个工作的代码块，由语句构成
#函数，可以理解成一个“行为”
'''
st=input('随机写一个表达式')
print(eval(st))
'''
#输入一个字符串，分别print每个字母
'''
def f(x):
    for i in range(len(st)):
        print(st[i])

st = str(input('输入字符：'))
f(st)
'''

#编写一个取绝对值的函数
'''
def f(x):
    if x>=0:
        return x
    else:
        return -x

'''

#f(x,y,z),函数内部算法：生成((x+y)*(x-y))**z
'''
def f(x,y,z):
    return ((x+y)*(x-y))**z
'''

#编写一个求平均值的函数
'''
def f(*m):
    print(m)
    return sum(m)/len(m)
'''


#定义一个函数，用于求矩形面积、圆形面积
'''
def f():
    l=float(input('长：'))
    w=float(input('宽：'))
    s1=l*w
    print('矩形面积为%.2f'%s1)
    r=float(input('半径：'))
    s2=r**2*3.1415926
    print('圆形面积为%.2f'%s2)

f()
'''

#求出以下函数∑_(k=0)^n▒〖ar^k (r≠0) 〗
'''
def f(a,r,n):
    s=0
    for k in range(n):        
        s=s+a*r**k
    return s

x=float(input('a='))
y=float(input('r='))
z=int(input('n='))

if(y==0):
    print('r不能为0')
else:
    print(f(x,y,z))
'''

#把输入结果变成一连串字典的key，并生成字典，需要用input输入

def dic():
    st=input('请输入一串字符，以逗号隔开：')

    k=st.split(',')
    print(dict.fromkeys(k))
    
dic()






































































    
