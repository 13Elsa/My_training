s=input("Enter String:").split()
key=int(input("Enter key value: "))
result=" "
for i in range(len(s)):
    result=result+s[i][key:len(s[i]):1]
    if i+1!=len(s):
        result=result+s[i+1][:key]+" "
result=result+s[0][:key]
print(result)
