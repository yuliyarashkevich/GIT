# Python. HW_1. 
# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)


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


