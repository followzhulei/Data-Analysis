import pickle

data1={'a':[1,2,3,4,[2,3,4]],'b':('string','aa'),'c':'hello'}

pic=open(r'C:\Users\ZL\Desktop\data.pkl','wb')
pickle.dump(data1,pic)
pic.close()
print('finished!')