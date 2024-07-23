
mylist = []
for r in range(10):
  mylist.append(r)
print(mylist)

mylist2 = [n for n in range(10)]
print(mylist2)

mylist2 = [2*n+1 for n in range(10)]
print(mylist2)

mylist2 = [2*n for n in range(10,100,5)]
print(mylist2)

mylist = [10, 45, 22, 89, 55, 34, 90 ]

y = [no for no in mylist if no >= 50]
print(y)

import numpy as np 
myarr = np.array([1,2,3,4,5]) 
b = [2 * no for no in myarr]
print(b)

def genPowLists(start, end):
  x = np.array([no for no in range(start, end+1)])
  y = x ** 2
  return (x, y)


(a, b) = genPowLists(2,9)
print(a)
print(b)

k = genPowLists(10,13)
print(k[0])
print(k[1])


