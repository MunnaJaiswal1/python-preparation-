txt="you have to PAY directly or indirectly everything."
print(len(txt))
if "pay" in txt:
    print("yes, pay is present in txt")
else:
    print("no, it is not present")
    
print(txt.upper())
print(txt.lower())

#OPERATOR
x=5
if(x>3 and x<10):
    print(x,"is true")
else:
    print("x is false",x)
 
 
y=110
print(y>100 and y<250)



#identify operator:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


