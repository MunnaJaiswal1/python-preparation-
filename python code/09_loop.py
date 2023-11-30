"""
#while loop
i=1
while i<6:
    print(i)
    i+=1
    
#break statement
i=1
while i<9:
    if i==5:
        break
    print(i)
    i+=1

#continue statement
i=1
while i<10:
    i+=1
    if i==6:
        continue
    print(i)
"""    
#for loop
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)
for x in fruits:
    if x=="banana":
        break
    print(x)
 