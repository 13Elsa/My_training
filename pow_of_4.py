n=int(input("Enter the number: "))
flag=0
for i in range(0,n+1):
    if(4**i==n):
        flag=1
        break
if(flag == 1):
    print("yes")
else:
    print("No")
