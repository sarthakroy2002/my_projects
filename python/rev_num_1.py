#
# Reverse a number using Python
#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#
a=int(input("Enter a number:"))
rev=0

while a>0:
    tmp=a%10
    rev=(rev*10)+tmp
    a//=10
print("The reversed number is:", rev)
