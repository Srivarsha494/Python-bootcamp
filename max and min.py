n=list(map(int,input().split()))
min=n[0]
max=n[0]
sum=0
for i  in range (len(n)):
    if(n[i]<min):
        min=n[i]
        print(min)
for i  in range (len(n)):        
    if(n[i]>max):
        max=n[i]
        print(max)
avg=(max+min)//2
for i in range (len(n)):
    n[i]=avg
print(n)    


