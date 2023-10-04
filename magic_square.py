n=int(input())
sq=[[0]*n for i in range(n)] #to insert 0 in every position of matrix
num=1
i=n//2                                            # i is rows and j is columns. We start from middle row i.e, n//2 and last column i.e, j=n-1
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:                       # if row is out of bound 
            i=n-1
        if j==n:                      # if column is out of bound
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:      #i is a list here
    #print(i)        # when you execute this the output contains brackets and commas. To avoid that, use *i
    print(*i)
print("Magic constant: ",n*(((n*n)+1)//2))
