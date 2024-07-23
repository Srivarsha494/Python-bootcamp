a=list(map(int,input().split()))
k=int(input())
n=int(input()) 
if (len(a)<k+n):
    print("error")
else:
    for i in range (len(a)):
      print(a[k+n],end=" ")
      break    

