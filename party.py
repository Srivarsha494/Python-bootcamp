n=int(input())
p=int(input())
t_r=240-p
count=0
for i in range (1,n+1):
    solve=i*5
    if solve <t_r and t_r>0:
        count+=1
    t_r-=solve
print(count)        