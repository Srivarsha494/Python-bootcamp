n=int(input("enter a number:"))
r=n**0.5
count=0
if n==1:
    print("not a prime number")
elif n==2:
    print("prime number")    
for i in range (2,int(r+1)):
    if n%i==0:
        count+=1
        break
if(count==0):
        print("prime number")
else:
    print("not a prime number")


