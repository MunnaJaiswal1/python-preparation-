a=4
b=5
print(a)
print(b)
c=a+b
print(c)

#casting
x=str(3)
y=int(5)
z=float(9)
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#variable name
#legal names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

myVariableName = "John" #camel case
MyVariableName = "John" #pascal case
my_variable_name = "John" #snake case

#multiple values:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
#x, y, z = fruits
print(fruits[0])
print(fruits[1])
print(fruits[2])

x, y, z = fruits
print(x)
print(y)
print(z)

#type conversion:
x=5 #int
y=4.0 #float
z=complex(5j)  #complex

#int to float
a=float(x)
print("integer to float",a)

#int to complex
b=complex(x)
print("integer to complex",b)

#float to int
a=int(y)
print("float to integer",a)
#float to complex
b=complex(y)
print("float to complex",b)

#complex to int
a=int(z)
print("complex to integer",a)

#complex to float
b=float(z)
print("complex to float",b)