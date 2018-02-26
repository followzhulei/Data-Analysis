#定义一个函数，可将输入的所有数字从大到小一次排序
'''
def f(x):
    n=x.split(',')
    m=[]
    for i in n:
        m.append(float(i))
    print(sorted(m,reverse=True))
    

x=input('输入数字列表：')
f(x)
'''

#统计输入任意字符中英文字母，空格，数字和其他字符的个数
'''
def f():
    s=input('随意输入字符：')
    alpha=0
    space=0
    digit=0
    pun=0

    for i in s:
        if i.isalpha():
            alpha=alpha+1
        elif i.isdigit():
            digit=digit+1
        elif i.isspace():
            space=space+1
        else:
            pun=pun+1

    print('字母有{}个，空格有{}个，数字有{}个，其他标点有{}个'.format(alpha,space,digit,pun))

f()
'''

#在分别输入年、月、日之后，判断出这一天是一年的第几天
y=int(input('年:\n'))
m=int(input('月:\n'))
d=int(input('日:\n'))

#闰年
month1=[0,31,60,91,121,152,182,213,244,274,305,335]
#非闰年
month2=[0,31,59,90,120,151,181,212,243,273,304,334]
def f():
    #判断是否是闰年
    #闰年
    if(y%400==0)or((y%100!=0) and (y%4==0)):
        s=month1[m-1]+d
        print('闰年，这一天是{}年的第{}天'.format(y,s))
    #非闰年
    else:
        s=month2[m-1]+d
        print('非闰年，这一天是{}年的第{}天'.format(y,s))

f()






























