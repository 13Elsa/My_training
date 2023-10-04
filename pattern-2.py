a=int(input())
    #straight pyramid
for i in range(0,a+1):
    print(" "*(a-i)+"* "*(i+1))
for i in range(0,a+1):
    #inverted pyramid
    print(" "*(i+1)+ "* "*(a-i))
for i in range(0,a+1):
    print(" "*(a-i)+"* "*(i+1))
