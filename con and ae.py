a=['a','e','i','o','u']
b='bcdfghjklmnpqrstvwxyz'
ca=0
cb=0
inp="hello world"
m=inp.lower()
for i in inp:
    if(i in a):
        ca+=1
for i in inp:
    if(i in b):
        cb+=1
print(ca)   
print(cb)      
for i in inp:
    if(i in b):
        print(i,end=" ")
       