#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#

##1

a=input("Enter text:")
x=open(r'C:\Users\lab.AUKDT0344\Desktop\test.txt','w+')
x.write(a)
x.close()

##2

a=input("Enter file path:")
x=open(a,'r')
print(x.read())
x.close()

##3

i=input("Enter file path of File 1:")
j=input("Enter file path of File 2:")
k=input("Enter file path of the file to write:")
x=open(i,'r')
y=open(j,'r')
z=open(k,'a+')
a=x.read()
b=y.read()
z.write(a)
z.write(b)
x.close()
y.close()
z.close()
