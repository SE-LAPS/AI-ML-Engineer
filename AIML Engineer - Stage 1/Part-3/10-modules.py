#importing a module
#import the module test as t

import test as t 
t.hello()
a, b, c, d = t.calc(40,2)
print(a)
print(b)
print(c)
print(d)


#importing a specific function and giving it an alias
from test import hello as greet
greet()
