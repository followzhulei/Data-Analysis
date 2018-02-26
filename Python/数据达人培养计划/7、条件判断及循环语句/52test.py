#Python代码的缩进规则：具有相同缩进的代码被视为代码块

'''
#判断成绩
while 1:
    score=input("请输入成绩：")
    score=float(score)

    if score >= 90:
        print("A")
    elif score >= 70:
        print("B")
    else:
        print("C")
'''

#判断语句代码，判断真假

while 1:
    w=input("请输入语句：")

    if eval(w) == True:
        print("真")
    else:
        print("假")


