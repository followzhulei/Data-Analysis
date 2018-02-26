path=r'C:\Users\ZL\Desktop\test.txt'
f=open(path,'r')
print(f.read())
f.seek(0)
f.close()
