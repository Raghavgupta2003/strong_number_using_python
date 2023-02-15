# strong number
n=input()

sum=0
for i in n:
    fact=1
    for j in range(1,int(i)+1):
        fact =j * fact
    sum =fact + sum
print(sum)
if sum==int(n):
    print("strong number")
else:
    print("not strong")
        
