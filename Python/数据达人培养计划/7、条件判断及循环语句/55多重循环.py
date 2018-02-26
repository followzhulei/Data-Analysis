#99乘法表
'''
for i in range(1,10):
    for j in range(1,10):
        m=i*j
        print(str(i)+'*'+str(j)+'='+str(m))
    print('\n')
'''

#现有‘abc’和‘123’两个字符串，快速打印出["a1","a2","b1","b2","c1","c2"]
'''
st1='abc'
st2='123'

n=len(st1)
m=[]

for i in range(n):
    for j in range(n):
         m.append(st1[i]+st2[j])

print(m)
'''

#随机书写一行字符串st，输入想查找的字母x，然后输出该字母所在st的字母位
'''
while True:
    st=input('随机输入一行字符串：')
    x=input("查找字母：")
    m=[]
    for i in range(len(st)):
        if(x==st[i]):
            m.append(i)
    print(m)
'''

#我要买一个热狗，分别询问①选择哪种小面包②是否要番茄酱③是否打包

print('输入a或者b')

x=input('a燕麦面包，b普通面包：')
y=input('a要番茄酱，b不要番茄酱：')
z=input('a打包，b不打包：')

if x=='a':
    if y=='a':
        if z=='a':
            print('燕麦+番茄酱+打包')
        else:
            print('燕麦+番茄酱')
    else:
        if z=='a':
            print('燕麦+打包')
        else:
            print('燕麦')
else:
    if y=='a':
        if z=='a':
            print('普通面包+番茄酱+打包')
        else:
            print('普通面包+番茄酱')
    else:
        if z=='a':
            print('普通面包+打包')
        else:
            print('普通面包')

       
        
