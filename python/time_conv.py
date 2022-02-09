#
# Write a Python program to accept time in seconds and convert it in HH:MM:SS format
#
# author: Sarthak Roy <sarthakroy2002@gmail.com>
#
sec = int(input("Enter time in seconds: " ))  
hr = sec //3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
print('The Time in HH:MM:SS format :',hr,':',min,':',sec) 
