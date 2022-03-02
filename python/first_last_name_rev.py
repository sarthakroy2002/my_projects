#
# Write  a accepts the user first and last name and print in reverse order
#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#
a=input("Enter your first name:- ")
b=input("Enter your last name:- ")
c=len(a)
d=len(b)
for i in range(d-1,-1,-1):
    print(b[i],end="")
else:
    print(" ",end="")
for i in range(c-1,-1,-1):
    print(a[i],end="")
  
