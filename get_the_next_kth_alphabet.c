a=input("Enter the character: ")
num=int(input("Enter the integer: "))
res=chr(ord(a)+num)
#print(res)
if ord(res)<90 and ord(res)>64 and ord(res)>90:
    op=ord(res)-26
    print(op)
elif ord(res)>96 and ord(res)<123 and ord(res)>123:
    op=ord(str)-26
    print(op)
elif (ord(res)<64 and ord(res)>91) or (ord(res)>96 and ord(res)<123):
    print(res)
else:
    print("INVALID INPUT")
