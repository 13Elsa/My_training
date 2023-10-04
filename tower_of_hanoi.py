def toh(n,source,aux,dest):
    if(n>0):
        toh(n-1,source,dest,aux) #------------------------------Here,destination is auxiliary and auxiliary is destination. We are mocing the n-1 disk not the n. Source to auxiliary with the help of destination.
        print(source,dest)
        toh(n-1,aux,source,dest) #------------------------------Auxiliary to destination with the help of source.
n=int(input("Enter the number of disks: "))
toh(n,'A','B','C')
