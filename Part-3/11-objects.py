#importing a class
from Person import Person 
p1 = Person("Nimal", 23)
p1.myfunc()

#importing a class
from Person import Person as P
p1 = P("Rajitha", 19)
p1.myfunc()

mylist = [Person("Ajith", 23), Person("Amali",18)]

for x in mylist:
  x.myfunc()