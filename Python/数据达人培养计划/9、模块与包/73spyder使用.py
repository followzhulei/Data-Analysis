# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd
data = xlrd.open_workbook('E:\\GitHub\\Data Analysis\\Python\\Excel\\73test.xlsx')
table = data.sheet_by_index(0)

nrows=table.nrows
ncols=table.ncols

k=list(table.row_values(0))
D=[]

for i in range(1,nrows):
    lst=table.row_values(i)
#    print(lst)
    v1=[]
    v1.extend([k[0],lst[0]])
    v2=[]
    v2.extend([k[1],lst[1]])
    m=(v1,v2)
#    print(m)
    d=dict(m)
#    print(d)
    D.append(d)

print(D)