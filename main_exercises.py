#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

l = [1, 2, 3]
a = 'abc'
 # l.extend(a)
 # print(l)
for i in a:
    l.append(i)
print(l)


# 3. Все чётные числа вывести в другой список
# l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
l = [1, 3, 4, 5, 8, 9, 10, 44, 22, 50, 79, 54, 28, 91]
n = []
for i in l:
    if i % 2 == 0:
        n.append(i)
print(n)


# 4. Все emails у которых есть слово test вывести в другой список

l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]
n = []
for i in l:
    if 'test' in i:
        n.append(i)
print(n)


# найти самое маленькое число в списке
l = [3, 0, 4, 5, 8, 9, 10, 44, 22, 50, -1, 79, 54, -28, 91]
min = l[0]
for i in l:
    if i < min:
        min = i
print(min)


# 6. Сравнить 2 строки без учёта регистра
# ==============================
a = 'abc'
b = 'aBc'
if a.lower() == b.lower():
    print(True)
else:
    print(False)


# 7. Проверить является ли массив подмножеством другого массива
l1 = [1,4,6]
l2 = [9,5,1,10,4,33,2,6,0,8]
j = 0
for i in l1:
    if i in l2:
        j+=1
if j == len(l1):
    print(True)
else:
    print(False)


# 8. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.

s1 = 'attachment'
s2 = 'qwertyuiopasdfghjklzxcvbnm'
for i in s2:
    count = 0
    for j in s1:
        if j == i:
            count+=1
    if count >1:
        print(j, 'встречается', count, 'раза')


# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.

def foo(string):
    return len(set(string)) == len(string)
print(foo('test'))
print(foo('tes'))


def digit_to_word(digit):
    if digit > 7:
        return 'Многабукаф'
    words_dict = {
        1: 'Одна буква',
        2: 'Две буквы',
        3: 'Три буквы',
        4: 'Четыре буквы',
        5: 'Пять букв',
        6: 'Шесть букв',
        7: 'Семь букв',
    }

    return words_dict[digit]


def no_duplicate_letters(string):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = {}
    words = string.split(' ')
    without_duplicates = True

    for word in words:
        result[word] = {}
        for i in alphabet:
            if word.lower().count(i) > 1:
                result[word][i] = word.lower().count(i)
                # print(result)
    for result_key, result_value in result.items():
        if result_value:
            for letter, count in result_value.items():
                print(f'{digit_to_word(count)} "{letter}" в "{result_key}"')
            without_duplicates = False

    return without_duplicates


print(no_duplicate_letters('Здравствуйте, Александра'), '\n')
print(no_duplicate_letters('Обороноспособность'), '\n')
print(no_duplicate_letters('Всегда дожимай до конца'), '\n')
