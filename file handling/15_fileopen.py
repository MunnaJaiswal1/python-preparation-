#first things is to do create a new file

#f=open("myfile.txt","x")#this will create a new file in same directory
"""
f=open("myfile.txt","w")
f.write("Hello, My name is: Munna kumar Chaudhary\n")
f.write("I am a Software Engineer\n")
f.write("And i am working hard to achieve my dreams")
f.close()

f=open("myfile.txt","r")
print(f.read())
print(f.read(2))
print(f.readline())
f.close()

f=open("myfile.txt","r")
for x in f:
    print(x)

#to delete that existing file
import os
os.remove("myfile.txt") #after doing that the file where we write and read that file was deleted parmanently.
"""
#f=open("D:\\myfile1.txt","a") #this will create a new file in D directory
f=open("D:\\myfile1.txt","w")
f.write("hello, its me your boss : Munna jaiswal")
f.close()

f=open("D:\\myfile1.txt","r")
print(f.read())
f.close()

import os
os.remove("D:\\myfile1.txt")