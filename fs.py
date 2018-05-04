# -*- coding:utf-8 -*-

with open ('file.txt','r') as f:
    dd3 = f.read()

a = {}
for i in dd3:
    if i not in a:
        a[i]=1
    else:
        a[i] +=1
print(dd3)
b = sorted(a.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
flag = ''
for i in b:
    flag += i[0]
print(flag)
