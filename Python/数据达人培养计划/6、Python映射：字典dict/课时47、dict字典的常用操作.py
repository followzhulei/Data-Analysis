name=["张三","李四","王二"]
num=["01","02","03"]
score=[90,80,70]

k=["姓名","学号","成绩"]

st1=dict.fromkeys(k)
print(st1)

st=[st1,st1.copy(),st1.copy()]
print(st)

for i in st:
    n=st.index(i)
    i["姓名"]=name[n]
    i["学号"]=num[n]
    i["成绩"]=score[n]

print(st)    
