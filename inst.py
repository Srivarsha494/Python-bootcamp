str="sri@var12/"
a=len(str) 
n="@/"
count=0
if(a<8):
    print("invaild")
for i in str:
    if i==n[0] or n[1] and i!=" ":
        count+=1
        break;
if count==1:
    
 if a>8 and a<12:
    print("weak password")    
 elif(a>12 and a<18):
    print("medium password")
 elif a==15:
    print ("strong password")
 else:
    print("please follow inst")  

          