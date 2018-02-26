f=open(r'C:\Users\ZL\Desktop\poi.txt','r')
f.seek(0)
m=[]

for line in f.readlines():
  #print(line)
  st1=line.split('：')
  #print(st1)
  name=st1[0]
  #print(name)
  st2=st1[1].split('，')
  #print(st2)
  add=st2[0]
  lng=float(st2[1])
  lat=float(st2[2])
  v=[['name',name],['lng',lng],['lat',lat],['add',add]]
  #print(v)
  d=dict(v)
  #print(d)
  m.append(d)

print(m)