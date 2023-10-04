def prnt(n):
    if(n==0):
        return 
    prnt(n-1)
    print(n)
n=int(input("Enter the input: "))
print(prnt(n))

#reverse order
def revprnt(n):
    if(n==0):
        return 
    print(n)
    revprnt(n-1)
print(revprnt(n))
