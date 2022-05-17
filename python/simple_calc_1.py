i=0
while i==0:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=int(input("Enter choice: 1- (+), 2- (-), 3- (*), 4- (/)"))
    x=0
    if(c==1):
        x=a+b
        print("The sum is:",x)
    elif(c==2):
        if(a>b):
            x=a-b
            print("The difference is:",x)
        elif(b>a):
            x=b-a
            print("The difference is:",x)
    elif(c==3):
        x=a*b
        print("The product is:",x)
    elif(c==4):
        x=a/b
        print("The quotient is:",x)
    else:
        print("Invalid Input")
    i=int(input("Enter 0 to start again, 1- to end:"))
    
