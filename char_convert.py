# chr function converts ascii value to string and ord function is to find ascii value of a string
str=input("Enter the character: ")
if ord(str)<90 and ord(str)>64:
    op=ord(str)-64
    print(op)
elif ord(str)>96 and ord(str)<123:
    op=ord(str)-96
    print(op)
else:
    print("INVALID INPUT")
#op=ord(str)-64
#print(op)
