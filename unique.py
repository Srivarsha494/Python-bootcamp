a=['a','e','i','o','u']
b='bcdfghjklmnpqrstvwxyz'
ans=""
inp="hello world"

m=inp.lower()                                                      
for i in inp:
    if(i not in a):
        ans+=1
print(ans)        