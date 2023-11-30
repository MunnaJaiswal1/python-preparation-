thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]

print(thislist.insert(2,"watermelon"))

#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
  
  #list comprehension
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

mylist=["apple","banana","cherry"]
newlist=[]
for x in fruits:
  newlist.append()
  
print(newlist)
  