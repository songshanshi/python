#coding:utf-8
with open('Basic-04.txt') as f:
    cipher = f.read()#读取txt内容
    plain = cipher.decode('hex')#16进制编码解密
    print plain