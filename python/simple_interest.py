#
# Write a Python program to accept principal amount, rate of interest and time in years. Now show the interest amount.
#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#
P= int(input("Enter Principal: " ))
R= int(input("Enter Rate per annum: " ))
T= int(input("Enter time : " ))
SI = P * R * T
am=P+SI
print('The Interest is:', SI)  
print('The Total Amount is: ', am)
