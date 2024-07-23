n=list(map(int,input().split()))
a=int(input())
sum=a*(a+1)//2
add=0
for i in  range (0,len(n)):
    add+=n[i]
print(sum-add)
 

