#string palindrome
str=input()
str2=list(str)
n=len(str)
#print(str2)
i=0
j=n-1
#for i in range(n):
#    if str2[i]==str2[j] and i>j:
#        i-=i
 #       j+=j
 #       if i=a=j:
 #           flag=1
 #   flag=0
#if(flag==1):
 #   print("PALINDROME")
#else:
#    print("NO")
while i<=j:
    if str[i]!=str[j]:
        print("PALINDROME")
        break
    i+=1
    j-=1
else:
    print("PALINDROME")
