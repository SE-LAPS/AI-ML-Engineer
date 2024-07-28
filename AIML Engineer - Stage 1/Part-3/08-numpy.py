#importing NumPy
import numpy as np # We are giving an alias to numpy as np, this is a general standard
a = np.array([1,2,3,4,5]) # defines a numpy array, here data have to be the same type
print(a)
# 2D Arrays
# more than one dimensions 
a = np.array([[1, 2], [3, 4],[5,6]]) 
print (a)

# dtype parameter 
a = np.array([1, 2, 3, 4, 5], dtype = float) 
# here the data type of the array 
# is given as float
print (a)

# Shape function
a = np.array([[1,2,3],[4,5,6]])
print(a.shape) # Dimensions of the array
# (2, 3) - 2D Array - with 2 rows and 3 columns each

a = np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]],
               [[13,14,15], [16,17,18]],
               [[17,18,19],[20,21,22]]])
print(a.shape) # Dimensions of the array
# (4,2,3) - 3D array as dimensions 4, 2, 3

# printing specific values
print(a[0]) # First element
print(a[1]) # Second element
print(a[0][0]) # First Dimension, 1st element
print(a[0][1]) # First Dimension, 2nd element
print(a[0][0][0]) # First Dimension, 1st element, 1st value
print(a[0][0][1]) # First Dimension, 1st element, 2nd value
print(a[0][0][2]) # First Dimension, 1st element, 3rd value

# Reshaping Arrays
# You can change the number of dimensions in the array
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print (b)
c = a.reshape(6)
print(c)

# A 2D array initialized to zero
x = np.zeros([10,5], dtype = int) 
print (x)

# A 2D array initialized to ones
x = np.ones([10,5], dtype = int) 
print (x)

# generate an array with start and stop parameters set 
x = np.arange(10,20,2) 
print (x)

# generate an array of evenly spaced numbers between a given range
x = np.linspace(10,20,5) 
print (x)

# Slicing
mylist = np.array([10,20,30,40,50,60,70,80,90,100])
print(mylist)
print(mylist[1]) # second element in array
print(mylist[2:5]) # prints 3rd, 4th and 5th elements in the array
print(mylist[2:]) # print all the elements from the 3rd element
print(mylist[:5]) # print all the elements upto the 5th element
print(mylist[len(mylist)-1])
print(mylist[-1])
print(mylist[-(len(mylist))])

# Array Manipulations
# In python you can perform direct array
#.  operations unlike other programming
#.  languages

a = np.array([10,20,30,40,50])
b = np.array([2, 3, 4, 5, 6])
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a * 2
print(c)
c = a * 2 + 5
print(c)
c = b ** 2
print(c)

print(a.sum())
print(a.min())
print(a.max())
print(a.mean())


