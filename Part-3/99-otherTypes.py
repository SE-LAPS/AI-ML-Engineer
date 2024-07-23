#list type
x = ["apple", "banana", "berry", 45, 56.7, True]
print(x)
print(type(x))

#tuple type
x = ("apple", "banana", "cherry", 45, 56.7, True)
print(x)
print(type(x))

x = range(6)
print(x) # range type
print(type(x))

y=tuple(x)
print(y) # typle type
print(type(y))

z=list(x)
print(z) # list type
print(type(z))

# show imutability of tuples

x = ["apple", "banana", "berry", 45, 56.7, True]
y = ("apple", "banana", "berry", 45, 56.7, True)
print(x)
print(y)
x[1] = "Mango"
print(x)
#y[1] = "Mango" # generates an error

# accessing list and tuples element by element

for item in x:
  print(item)

for item in y:
  print(item)

# combining lists together
z = ["honda", "toyota", "tesla"]
x = x + z
print(x)

z = ("honda", "toyota", "tesla")
y = y + z
print(y)

# Basic list operations
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[1])
mylist = [10,20,30,40,50,60,70,80,90,100]
print(mylist)
print(mylist[1]) # second element in list
print(mylist[2:5]) # prints 3rd, 4th and 5th elements in the list
print(mylist[2:]) # print all the elements from the 3rd element
print(mylist[:5]) # print all the elements upto the 5th element

