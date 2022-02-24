#
# Palindrome number using Python
#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#
a=int(input("Enter a number:"))
rev=0
b=a
while a>0:
    tmp=a%10
    rev=(rev*10)+tmp
    a//=10
if b==rev:
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")
    
