import os

a="Sudhanwa:Bokade"
b="Milind:Bokade"


f=open('test.txt','a')
f.write(a)
f.write(",")
f.write(b)
f.write(",")
f.close()


f=open('test.txt','r')


for i in f.readlines():
    for k in i.split(","):
        print(k)
        # q,w=k.split(":")
        # print(q,w)
        
    
    