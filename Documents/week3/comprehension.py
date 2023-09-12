# comrehension - генерация последовательностей в одну строку используя цикл
# Также его называют синтаксическим сахаром

# index = 0
# for i in range (1,11)   синтаксический сахар это то, что делает код проще и легче
# index +=1
# index = index + 1

# Основной целью использования как list, dict comprehension явл упрощение и повышение
# читаемости кода

# list comprehension(генераторы) - это упрощенный подход к созданию списка, который задействует цикл for
# а также мы можем использовать if else операторы
# под капотом генератор списка также исп. цикл for, но по скорости он быстрее потому что 
# не исп. метод append

# list1 = []
# for i in range(1,11):
#     list1.append(i**2)
# print(list1)

# list1 = (i ** 2 for i in range(1,11))
# print(list(list1))

# list1 = [i ** 2 for i in range(1,11)]
# print(list1) #перевод снизу

# i **2 результат for элемент in итерируемый обьект

# import time 
# start_time = time.time()
# list1 = []
# for i in range(100):
#     list1.append(i)
# time1 = time.time() - start_time
# print(time1)

# start_time1 = time.time() # 11:42
# list2 = [i for i in range(100)] #код работы
# time2 = time.time() - start_time1 # 11:43 - 11:42
# print(time2)

# list1 = [i for i in range(1,11) if not i%2]
# print(list1)

# list1 = [i for i in range(0,11,2)]
# print(list1)

# list1 = ['hello' for i in range(10)]
# print(list1)

# print = ([input() for i in range(10)])

# если в усовии нужен else, то все условия пишется до for 

# list1 = ['нечетное' if i % 2 else 'четное' for i in range(1,11)]
# print(list1)

# list1 = [1, 'Hello', 2, 'a', 4.0, '7', 8]
# a = ['нечетное' if i % 2 else 'четное' for i in list1 if type(i) == int or type(i) == float]
# print(a)

# SET COMPREHENSION
# Разница с list comprehension что выходные данные не содержат дубликатов

# list1 = [1,2,3,4,5,6,7,8,8,8,8,8,4]
# set1 = {i for i in list1}
# print(set1)

# set1 = set()
# for i  in list_:
#     set.add(i)
#     print(set)

# dict comprehension - аналогично создаются, но надо указывать ключ и значение

# squares = {i:i**i for i in range(10)}
# print(squares)

# dict = {}
# for i in range(10):
#     squares.update({i: i**i})
# print(squares)

# list_ = {1,2,3,4,5,6,7,8}
# dict_ = {i: list_.count(i) for i in list_}
# print(dict_)

# d = {'a': 2, 'c':3}
# dict_ = {k: 'четное' if v %2 ==0 else 'нечетное' for k,v in d.items()}
# print(dict_)

# dict = {10}
# dict1 = {k: 'ключи' v: 'значения' for k,v in dict.items() type(str)} создать словарь ключи от 1 до 10 а значения эьт же числа но с типом данных str
# print(dict1)

# dict1 = {i: str(i) for }

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = {list1[index]:list2[index] for index in range(len(list1))}
# print(list3)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {key: value for key,value in dict1.items()}
# print(dict2)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict2)
# СОЗДАЙТЕ СЛОВАРЬ ГДЕ ЗНАЧЕНИЕМ БУДЕТ СУММА ИЗ ЗНАЧЕНИЙ
# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }
# dict2 = {key: sum(value) for key, value in dict1.items()}
# print(dict2)

# СОЗДАЙТЕ СПИСОК СОСТ ИЗ 10 СПИСКОВ, В КОТОРОМ 'HELLO WORLD' ПОВТОРЯЕТСЯ ПО 5

# list1 = [['helloworld' for i  in range(5)] for i in range(10)]
# print(list1)

# напишите программу которая запрашивает число и выводит сумму его

# user = input('enter int: ')
# summa = 0
# for i in user:
#     summa += int(i)
# print(summa)