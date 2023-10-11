n=int(input())
start=0
last=n//2
floor=-1
while start<=last:
    mid=(start+last)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        start=mid+1
    else:
        last=mid-1
print(floor)
