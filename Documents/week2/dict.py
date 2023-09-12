# dict1 = {}
# dict2 = dict()
# print(type(dict1))
# print(type(dict2))

# my_dict = {
#     'name': 'Erlan',
#     'surname': 'Jukeshovich',
#     'age': 26
# }
# print(my_dict)

# Альтернтивные способы создания словаря

# my_dict = dict(a=1, b=2, c=3)
# print(my_dict)
# my_dict2 = {'a':1, 'b': 2, 'c': 3}
# print(my_dict2)
# ЕСЛИ МЫ ХОТИМ СОЗДАТЬ СЛОВАРЬ С ПОМОЩЬЮ dict(),
# ТО ДЛЯ КЛЮЧЕЙ РАБОТАЕТ ТЕ ЖЕ ПРАВИЛА ЧТО И ДЛЯ ПЕРЕМЕННЫХ

# my_list = [['m',1],['a',2],['k',3]]
# my_dict = dict(my_list)
# print(my_dict)

# АЛЬТЕРНАТИВНЫЕ СПОСОБЫ СОЗДАНИЯ СЛОВАРЯ МОГУТ МЕЖДУ СОБОЙ СОЕДИНЯТЬСЯ

# my_list = [['m',1],['a',2],['k',3]]
# my_dict = dict(my_list, a=1, b=2, c=3)
# print(my_dict) 

# dict_ = {1: 'Makers', '2': True, False: []}
# print(dict_)

# КЛЮЧАМИ В СЛОВАРЕ ДОЛЖНЫ БЫТЬ НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ
# А ЗНАЧЕНИЯ MOGUT BIT LUBYE TIPY DANNYX

# НЕУПОРЯДОЧЕННЫЕ ТИПЫ ДАННЫХ ИМЕЮТ ТАКЖЕ СЛОВАРИ
# НО НАЧИНАЯ С ВЕРСИИ 3.6 ОНИ СТАЛИ УПОРЯДОЧЕННЫМИ

# dict1 = {'Alice': 'black',
#         'Sara': 'yellow',
#          'Sam': 'green'}
# # print(dict1['Sara'])
# dict1['Sam'] = 'pink'
# dict1['Rachel'] = 'blue'
# print(dict1)

# ========================МЕТОДЫ СЛОВАРЕЙ====================
#                     method get(key, None)
# ЕСЛИ ПРИ ИСПОЛЬЗОВАНИИ get(key) У НАС НЕТУ ЭТОГО КЛЮЧА,
# ТО НАМ ВЫДАЕТСЯ None
# dict1 = {1: 'Tom', 2: 'John', 3: 'Alice'}
# print(dict1.get(4, 'we dont have this key'))
# print(dict1[3])
                # ====method clear()====
# ЭТОТ МЕТОД ПОЛНОСТЬЮ ОЧИЩАЕТ НАШ СЛОВАРЬ  
# dict1 = {1: 'Tom', 2: 'John', 3: 'Alice'}
# print(dict1)
# dict1.clear()
# print(dict1)
                # ====METHOD COPY()====
# dict1 = {1: 'Tom', 2: 'John', 3: 'Alice'}
# dict2 = dict1.copy()
# print(dict2)
# dict1[2] = 'Rachel'
# print(dict1)
# print(dict2)

# # list_[1] = "makers"

            #==== method pop(key,default)=====
# dict1 = {'name': 'Kate', 'height': 170, 'weight': 50}
# deleted = dict1.pop('name', 'no this key')
# print(dict1)   
# print(deleted)

#           ====method popitem()=======
# УДАЛЯЕТ РАНДОМНЫЙ ЭЛЕМЕНТ, НО В СЛУЧАЕ В ВЕРСИЕЙ ВЫШЕ 3.6
# ОН УДАЛЯЕТ ПОСЛЕДНИЙ ЭЛЕМЕНТ

# УДАЛЯЕТ ЛЮБУЮ ПАРУ КЛЮЧ ЗНАЧЕНИЕ В СЛОВАРЕ
# ТАК КАК ОН НЕУПОРЯДОСЕН
# POPITEM() ТАКЖЕ ВОЗВРЩАЕТ ЗНАЧЕНИЕ УДАЛЕННОГО КЛЮЧА

# dict1 = {'name': 'Kate', 'height': 170, 'weight': 50}
# deleted = dict1.popitem()
# print(dict1)
# print(deleted)

#            ====method setdefault(key, default)========
# ОН ВОЗВРАЩАЕТ ЗНАЧЕНИЕ КЛЮЧА КАК И МЕТОД GET
# dict1 = dict(a=1, b=2, c=3)
# print(dict1.setdefault('d', 5))
# print(dict1)

                # =====method update()=======
# ОБЬЕДИНЯЕТ ДВА СЛОВАРЯ 

# dict1 = {1: 'Tom', 2: 'Alice'}
# dict2 = {2: 'Tomas', 4: 'Allan'}
# dict1.update(dict2)
# print(dict1)
# print(dict2)
# ЕСЛИ ПРИ ОБЬЕДИНЕНИИ ДВУХ СЛОВАРЕЙ МЫ ИМЕЕМ 
# одинаковый ключ, то ключ перезаписывается

#        =======method fromkeys(seq,value)=======
numbers = [1,2,3,4,5]
new_dict = dict.fromkeys(numbers, 'makers')
print(new_dict)

# numbers = list('makers')
# new_dict = dict.fromkeys(numbers, 'makers')
# print(new_dict)
# он присваивает к элементам значения и создается словарь 
# и присваивает только два элемента не больше


# =====================ПЕРЕБОР ЭЛЕМЕНТОВ СЛОВАРЯ==================

# items(), keys(), values()

# dict1 = {'name': 'Erlan', 'height': 170, 'weight': 80}
# # print(dict1.items())
# print(dict1.keys())
# print(dict1.values())

# contacts = {
#     'Alice': '+996708685040',
#     'Tom': '+996708685050',
#     'Bob': '+996708685060'
# }
# for key, value in contacts.items():
#     print(f'name: {key} tel: {value}')

# For по умолчанию будет выдавать только ключи
#  method .items() позволяет перебирать как ключи так и значения

# contacts = {
#     'Alice': '+996708685040',
#     'Tom': '+996708685050',
#     'Bob': '+996708685060'
# }
# for key in contacts.keys():
#     print(f'name: {key}')
# #  method .key() позволяет перебирать только ключи

# contacts = {
#     'Alice': '+996708685040',
#     'Tom': '+996708685050',
#     'Bob': '+996708685060'
# }
# for value in contacts.values():
#     print(f'tel: {value}')
# #  method .value() позволяет перебирать только значения

# ==============ВЛОЖЕННЫЕ СЛОВАРИ==========
# n_dict = {
#     'Makers': {
#         'Aibek': 23,
#         'Adilet': 27,
#         'Aidai': 21,
#         'Nurbek': {
#             'age': 18,
#             'height': 190,
#             'weight': 80
#         }
#     }
# }
# print(n_dict['Makers']['Nurbek']['height'])

# seasons = {'лето':'жара', 'осень':'дождь', 'весна':'солнечно'} 
# seasons['весна'] = 'дождь' 
# print(seasons['весна']) 

# a = {'x': 1, 'y': 2, 'z': 1}
# a.update({'a': 5})
# a.pop(a)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# =============Вывести в словаре только значения с элементами стр=======================
# some_dict = {0: False, 1: 'это', 2: 'строка', 3: True} 
# for k, v in list(some_dict.items()):     
#      if type(v) != str:         
#          del some_dict[k]  
# print(some_dict) 
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = list(a)
# print(b)

# Задание 9

# Создайте словарь a с числовыми значениями. Создайте новый словарь b, такой же как словарь а, но все четные значения замените на 2.
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k, v in a.items():
#     if v %2 == 0:
#         b.setdefault(k,2)
#     else:
#         b.setdefault(k,v)
# print(b)

# 23.08.23 КОРТЕЖИ TUPLE

# tuple - неизменяемый тип данных, индексипуемый, упорядоченный, итерируемый.
# ПРедназначен для хранения любых данных(в целом не отличаются от списков, просто их нельзя изменить)
# Занимают меньше памяти чем списки

# Итерация (лат. iteratio — повторение) — повторение какого-либо действия. 
# Итерация в математике — повторное применение какой-либо математической операции.
#  применяется к циклами

# tuple1 = ()
# print(type(tuple1))

# tuple1 = (1,2,3,[1,2,3],{"1": 2})
# tuple1[3].append(4)
# print(tuple1)

# tuple = 1,2,3       -> это кортеж
# print(type(tuple))

# t = tuple('hrllo')    #-> выводит в кортеже каждую букву отдельно 
# print(t)

# ================== vethod==================

# count считает колво элементов

# tuple1 = (1,2,3,4,5,5,6,7)
# print(tuple1.count(5))

# t1 = ('hello','hello')
# print(t1.count('hello'))

# t1 = 1,2,3,4,5,6
# print(t1.index(3))

# ДОбавить в списки в корткжк в конец число 2
# tuple1 = ([1,2,3], 1, 'h', [4,5,6], '1', 2, [7,8,9])
# for i in tuple1:
#     if type(i)==list:
#         i.append(2)
#         print(i)


#                                                ================СЛОВАРИ========================

# словари  - это одна из наиболее часто используемых структур данных, позволяющий хранить обьекты.
# словарь - изменяемый, неидексируемый, упорядоченный, итерируемый тип данных
# в котором элементы хранятся в в сиде пары ключ,значение

# dict1 = {'a': 'helo', 'b': 'World'}
# print(dict1)

# dict1 = {1: 'hello', 2:[1,2,2,3], 4.5:{'s':3}}
# print(dict1[1])

# dict1 = {
#     'name': 'Tom',
#     'age': 26,
#     'hobby': ['fishing','football']
# }
# print(dict1['name'])

# dict() - второй способ создания словаря
# dict2 = dict([('key', 'value'), ('key2', 'value2')])
# print(dict2)

# dict3 = dict(['ab', 'cd', 'de'])
# print(dict3)

# dict1 = dict() # - третий способ создания словаря
# dict1['key1'] = 'value'
# print(dict1)

# dct = dict(age=25)
# dct['age'] = 26
# print(dct)

#                                       ============методы словаря==================

# clear() щчищает словарь

# dct = {'name': 'John', 'age': 25}
# dct.clear()
# print(dct)

# import copy

# copy() - возвращает копию словаря
# dct = {'name': 'John', 'age': 25, 'hobby':['basket','vollty']}
# dct2 = dct.copy()
# dct2['hobby'][1] = 'football'
# print(dct2)

# fromkeys[object, value] - создает словарь с ключами из jbject и значением Value
# для всех ключей 
# если не передать value то значение будет None

# list1 = ['name', 'age', 'hobby']
# dct = dict.fromkeys(list, 'h1')
# print(dct)

# methods получения элементов словаря

# dict1 = {'name': 'erlan', 'age': 25}
# print(dict1.get('ag', 'no duch key'))
# print(dict1['age'])

# update() method - добавляет в наш словарь наш словарь


# dict1 = {'name': 'erlan', 'age': 25}
# dict2 = {'hobby':['football','basketball']}
# dict1.update(dict2)
# print(dict1)


# setdefault - получение значений
# работает точно также как get() но если такого ключа нет он создает новую

# dict1 = {'name': 'erlan', 'age': 25}
# dict1.setdefault('hovbby')
# print(dict1)

# method value() - выводит значение словаря

# dict1 = {'name': 'erlan', 'age': 25}
# print(list(dict1.values()))

# keys() - выводит ключи которые в словаре

# dict1 = {'name': 'erlan', 'age': 25}
# print(list(dict1.keys()))

# method items() - выводит все ключи и значения в словаре

# dict1 = {'name': 'erlan', 'age': 25}
# print(dict1.items())

# удаление элементов

# method pop(key, [message]) удалфяет пару ключ значение и возвращает значение
# если ключа нет, то возвращвет message 

# dcit1 = {
#     'name': 'Erlan',
#     'age': 25
# }
# removed = dcit1.pop('name')
# print(removed)
# print(dcit1)

# popitem() -> удаляет и возвращает пару ключ значение
# удаляет послежнюю словарную пару

# dict1 = {
#     'name': 'Erlan',
#     'age': 25
# }
# removed = dict1.popitem('name')
# print(removed)


# вытащить четные из словаря и присвоить им 0
# dict1 = {'a':1, 'b':2, 'c':3,'d':4, 'e':5,'f':6}
# for k, v in dict1.items():
#     if v %2 == 0:
#         dict1[k] = 0
# print(dict1)

# dict1 = {'name': None, 'surname': None,'age': None,'hobby': None,}       неправильго
# for v in dict1.values():
#     if v = None:
#         len(dict1[v])
# print(dict1)

# заменить None на 'ключ'
# dict1 = {'name': None, 'surname': None,'age': None,'hobby': None,}
# for key in dict1.keys():
#     print(key, 'ключ')
#     dict1[key] = len(key)


# dict1 = {'a':20, 'b':30,'c':40,'d':50,'e':60,}
# grade = 0
# for value in dict1.values():
#     grade += value
# average = grade / len(dict1)
# dict1['average'] = average 
# print(dict1)   

