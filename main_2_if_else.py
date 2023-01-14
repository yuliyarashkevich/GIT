int_item = 10
comp_item = 18
mult_in = int_item*2
item_2 = True
item_3 = False
item_4 = 0
item_5 = 1

usd_item = 'usd'
usd_usd_rate = 1

eur_item = 'eur'
usd_eur_rate = 0.86

uah_item = 'uah'
usd_uah_rate = 0.91

chf_item = 'chf'
usd_chf_rate = 0.91

rub_item = 'rub'
usd_rub_rate = 71.88

byn_item = 'byn'
usd_byn_rate = 2.46

if mult_in > comp_item:
    print("Переменная mult_in больше", comp_item)

div_int = int_item/2
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)

item_1 = 10+int_item
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)

if item_2:
    print("Переменная item_2 =", item_2)
else:
    print("Переменная item_2 =", item_3)

if item_3:
    print("Переменная item_3 =", item_2)
else:
    print("Переменная item_3 =", item_3)

if item_5:
    print("Переменная item_5 =", item_5)
else:
    print("Переменная item_4 =", item_4)

if item_4:
    print("Переменная item_4 =", item_5)
else:
    print("Переменная item_4 =", item_4)

currency_convertor = item_2

if currency_convertor:
   # print ("Выполняем следующие шаги задания")
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == 'eur':
            currency_result = target_currency_amount/usd_eur_rate
            print(target_currency_amount, eur_item, "=", currency_result, usd_item)
    elif target_currency == 'uah':
            currency_result = target_currency_amount/usd_uah_rate
            print(target_currency_amount, uah_item, "=", currency_result, usd_item)
    elif target_currency == 'chf':
            currency_result = target_currency_amount/usd_chf_rate
            print(target_currency_amount, chf_item, "=", currency_result, usd_item)
    elif target_currency == 'rub':
            currency_result = target_currency_amount / usd_rub_rate
            print(target_currency_amount, rub_item, "=", currency_result, usd_item)
    elif target_currency == 'byn':
            currency_result = target_currency_amount / usd_byn_rate
            print(target_currency_amount, byn_item, "=", currency_result, usd_item)
else:
    print("Переменная currency_convertor =", item_3)
    
    
# Python old HW 3 if else elif
# 1. Создать переменную int_item со значением 10
# 2. Создать переменную comp_item со значением 18
# 3. Создать переменную mult_int в которй умножите int_item на 2
# 4. Создать переменную item_2 со значением True
# 5. Создать переменную item_3 со значением False
# 6. Создать переменную item_4 со значением 0
# 7. Создать переменную item_5 со значением 1
# 8. Создать переменную usd_item со значением ‘usd’
# 9. Создать переменную usd_usd_rate со значением 1
# 10. Создать переменную eur_item со значением ‘eur’
# 11. Создать переменную usd_eur_rate со значением 0.86
# 12. Создать переменную uah_item со значением ‘uah’
# 13. Создать переменную usd_uah_rate со значением 26.23
# 14. Создать переменную chf_item со значением ‘chf’
# 15. Создать переменную usd_chf_rate со значением 0.91
# 16. Создать переменную rub_item со значением ‘rub’
# 17. Создать переменную usd_rub_rate со значением 71.88
# 18. Создать переменную byn_item со значением ‘byn’
# 19. Создать переменную usd_byn_rate со значением 2.46
# 20. Сделать if в котором будет условие: если mult_int больше comp_item, то вывести в консоль (“Переменная mult_int больше”, comp_item)
# 21. Создать переменную div_int в которй разделить int_item на 2
# 22. Сделать if в котором будет условие: если div_int меньше comp_item, то вывести в консоль (“Переменная div_int меньше”, comp_item)
# 23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
# 24. Сделать if в котором будет условие: если item_1 меньше comp_item, то вывести в консоль (“Переменная item_1 меньше”, comp_item), иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
# 25. Сделать if в котором будет условие: если item_2, то вывести в консоль (“Переменная item_2 = ”, item_2), иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
# 26. Сделать if в котором будет условие: если item_3, то вывести в консоль (“Переменная item_3 = ”, item_2), иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
# 27. Сделать if в котором будет условие: если item_5, то вывести в консоль (“Переменная item_5 = ”, item_5), иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
# 28. Сделать if в котором будет условие: если item_4, то вывести в консоль (“Переменная item_4 = ”, item_5), иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
# 29. Создать переменную currency_convertor со значением item_2
# 30. Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания, иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
# 31. Внутри if currency_convertor сделать следующие If условия :
                    # 31.1 Создать переменную currency_usd со значением usd_item
                    # 31.1 Создать переменную currency_usd со значением usd_item
                    # 31.2 Создать переменную target_currency со значением eur_item
                    # 31.3 Создать переменную target_currency_amount значением 50
                    # 31.4 Создать переменную currency_result со значением 0
                    # 31.4 Сделать if в котором будет условие: если target_currency равен ‘eur’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_eur_rate. Результат вывести в консоль (target_currency_amount, eur_item, “=”, currency_result, usd_item)
                    # 31.5 Сделать elif в котором будет условие: если target_currency равен ‘uah’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_uah_rate. Результат вывести в консоль (target_currency_amount, uah_item, “=”, currency_result, uah_item)
                    # 31.6 Сделать elif с остальными валютами
                    # 31.7 Последним оставить else, при выполнений которого в консоль выведется (“Unknow currency”)
