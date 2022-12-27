from typing import Dict

name = 'Julia'
age = 33
a = 55.5
b = bytes(2)
c = [1, 4.4, 'hello']
d = (10, 20, 30)
e = {1, 2, 3, 1, 2, 3}
f = {1, 4, 2, 3, 1, 2, 3}
g = frozenset(f)
location = {'country': 'Belarus', 'town':'Minsk'}

print(type(name),name,
      type(age),age,
      type(a),a,
      type (b),b,
      type (c),c,
      type(d),d,
      type(e),e,
      type(g), g,
      type(location),location)

firstname = 'yulia'
lastname = 'rashkevich'
fl = firstname + ' ' + lastname
print(fl)

age = 33

print(firstname,age)

print(firstname + " " + str(age))


