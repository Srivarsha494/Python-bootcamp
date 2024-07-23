amount=750
no_apple=int(input())
no_banana=12*int(input())
no_oranges=int(input())
cost_apple=15
cost_banana=8
cost_oranges=5
am=cost_apple*no_apple
bs=cost_banana*no_banana
os=cost_oranges*no_oranges
sum=am+bs+os
diff=amount-sum
if diff==0:
    print("not cheated")
else:
    print("cheated")    