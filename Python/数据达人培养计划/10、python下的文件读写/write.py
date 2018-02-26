path=r'C:\Users\ZL\Desktop'

'''
f=open(path+'\\test.txt','w',encoding='utf8')

f.write('hello world')
f.write('asdasdas')#不覆盖
f.close()
'''
'''
lst=['a','b','c','d','e']
with open(path+'\\test.txt','w',encoding='utf8') as f:
    f.write('hello world')
    f.writelines(lst)

print('finished!')
'''
n=list(range(1,11))
m=['a','b','c','d','e','f','g','h','i','j']
l=[]
with open(path+'\\test.txt','w',encoding='utf8') as f:
    for i in range(len(n)):
        f.writelines([str(n[i]),',',m[i],'\n'])

print('finished!')
