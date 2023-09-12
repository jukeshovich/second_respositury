#print("hello world")

#NoneType -> ничего
#Boolean true False
#str
#float
#complex

#4. Списковые типы данных
#a. list() - массив - неизменяемый
#b. tuple() - кортеж - (1,2,3,4,5, True, False)

#5. str - строки - "Hello world"

#6. set() - множества - {1,2,3,4,5, None, False, True}

#7. frozenset() - замороженное множество {1,2,3,4,5, None, False, True, True}

#8. dict() - словарь содержит данные в виде пары ключ/знчение
# {1:"a"} {"id":1} {"usename: erlan"} {"password": 123456}

# В ПИТОНЕ ЕСТЬ ТОЛЬКО ДВА ТИПА ДАННЫХ ИЗМЕНЯЕМЫЙ И НЕИЗМЕНЯЕМЫЙ

# неизменемый тип данных
# 1. NoneType
# 2. Boolean
# 3. int()
# 4. float()
# 5. complex()
# 6. tuple()
# 7. str()
# 8. frozenset()

# изменяемый тип данных
# 1. list()
# 2. set()
# 3. dict()

#-----------------переменные--------------
# переменные - это ссылка на ячейку в памяти в которой хранится какая то информация и в переменной мы можем хранить разные типы данных

# как должны называться 
#название переменных в Python должны начинатсья с алфавитного символа или со знаком подчеркивания

# a = 1
# x = 2
# _x = 3
# age1 = 2
# age_2 = 3

# имя не может начинаться с цифры или с символов
# 2age = 2 - нельзя
# %age = 2 - нельзя
# нельзя использовать зарезрвированные слова
# if else for while

# number = int()
# string = str()
# list_of_numbers = list()
# print(number)
# print(string)
# print(list_of_numbers)

# Python явлется языком с динамической типизацией
# в языке С мы не модем поменять переменные
# int number = 2

# '=================ВВод и вывод данных=============='



#===================ВВОД И ВЫОД ДАННЫХ===============
# + - сложение
# a = 10
# b = 5
# z = a+b
# print(z)

# # '//' - целочисленное деление (оставляет только целое число)
# a = 5
# b = 2
# print(a//b) 

# "*" - умножение

# '%' - остаток  от деления (деление при котором мы получаем остаток)

# a = 2
# b = 4
# print(a%b)

# "**" - возведение в степень

# 25 ** 0.5 - квадратный корень числа

# модуль числа - из отрицательного в полодительное
# abs(-2) будет просто 2

# pow()
# 1. возводит в степень 
# 2. возвращает остаток от деления(результат первых двух чисел на третье)
# print(pow(2,3))
# print(pow(2,3,4)) (2**3)%4

# divmod - функция принимает два чила и возвращает два числа
# 1. результат целочисленного значения //
# 2. остаток от деления %
# divmod(2,3) 2//3, 2%3

# round - функция которая округляет число 
# round(5.6) 6
# round(3.5) 4
# round(4.4) 4
# print(round(7.49, 3))

# можно уквзвть сколько цифр после запятой оставить

#print(round(pi,3))

# import math 
# dir() - возвращает функцию для нахождения корня числа

#print(math.sqrt(36))

# мнодественные присваивания

# x = 1
# y = 2
# z = 3
# print(x)

# x,y,z = y,z,x

# Дана переменная с радиусом окружности, найдите периметр и площадь окружности 

# from math import sqrt, pi
# a = input (int("введите первое значение"))
# b = input (int("введите второе значение"))
# print(math.sqrt,pi)

# from math import pi
# r = int(input("Введите радиус: "))
# result_S = pi * (r**2)
# result_P = 2 * pi * r

# print("Площадь окружности", result_S)
# print("Периметр окружнсти", result_P)

# 17.08.2023

# 1. строки неизменяемый тип данных который предназначен для хранения текста
# заключаются в одинарные или двойные кавычки

# string1 = 'строка с одинарными кавычками'
# string2 = "строка с двойными кавычками"
# string3 = "'Makers'"
# string = '''
# adadafsfefefe (тут можно ставить любые кавычки)
# '''
# print(string)

# print('Hello\nworld') в принте занимает две ячейки 
# a = 'Hello '
# b = 'World'
# print(a + b) конкатенация строк

# Дублирование строк
# a = 'Hello'
# print(a*4) будет 4 раза Hello

# ===================ФОРМАТИРОВАНИЕ СТРОК======================
# 1.  С ИСПОЛЬЗОВАНИЕМ %
# 2. С ИСПОЛЬЗОВАНИЕМ МЕТОДА .format()
# 3. ИНТЕРПОЛЯЦИЯ СТРОК (f-строки)

# %
# name = input('ВВЕДИТЕ ВАШЕ ИМЯ: ')
# result = "Hello, %s " %name
# print(result)

# .format(переменная)
# name = 'atai'
# name1 = 'gohn'
# name2 = 'alan'
# result = 'hello, {}, {}, {}'.format(name, name1, name2)
# result = 'hello, {2}, {0}, {1}'.format(name, name1, name2)
# result = 'hello, {name}, {name1}, {name2}'.format(name = 'atai, name1 = 'gohn', name2 = 'alan')
# print(result)

# ИНТЕРПОЛЯЦИЯ СТРОК f строки (форматирование)
# name = input('Введите ваше имя: ')
# result = f'Hello,{name}'
# print(result)

# ===============МЕТОДЫ СТРОК====================
# МЕТОДЫ ТИПОВ ДАННЫХ - ФУНКЦИИ, К КОТОРЫМ МЫ ОБРАЩАЕИМСЯ ЧЕРЕЗ ТОЧКУ
# МЕТОДЫ НА is 
# все что начинается на is возвращает TRue False

# string - '1234'
# print(string.isdigit())
# isdigit() - возвращает TRue ecли строка полностью состоит из цифр

# isalpha() -возвращает True если строка полностью состиот из букв
# print(string.isalpha())

# isalnum() СОСТОИТ ли строка из цифр и букв
# print(string.isalnum)

# string ='asd123'
# islower() - состоит ли строка из символов нижнего регистпа
# isupper() - состоит ли строка из символов заглавных букв

# isspace() - состоит ли строка из неотображаемых данных 

# istitle() -  начинаются ли слова в строке с заглавной буквы

# print(dir(str)) посмотреть все методы типов данных

# lower() - переводит целую строку в нижний регистр
# print('HELLO'.lower())

# upper() - переводит целую строку в верхний регистр
# a = 'assa'
# print(a.upper())

# swapcase() - переводит символы в противоположный регистр
# a = 'Hello World'
# print(a.swapcase())

# title() - переводит первую букву слова в строке в верхний регистр 
# a = 'hello'
# print(a.title())

# a = 'HELLO'
# print(a.title())

# strip() - убирает пробелы, символы в начале и в конце строки
# a = '   Hello World    '
# print(a.strip())

# lstrip() rstrip() - убирает пробелы или символы с левой и правой стороны

# replace( old,new) - меняет значение old на new
# a = 'ha ha ha ha ha ha'
# print(a.replace('ha', 'he', 3))
# replace - сщздает новую строку и не меняет к переменному к которому мы обращемся

# split() - делит строку по разделителю и возвращает массив list()
# a = 'Hello,World'
# b = a.split(',')
# print(b)

# ИНДЕКС - ПЛРЯДКОВЫЙ НОМЕР СИМВОЛОВ В СТРОКЕ 
# 'hELLO WORLD'

# H E L L O W O R L
# 0 1 2 3 4 5 6 7 8 

# string = 'hello world'
# print(string[0])
# print(string[10])
# print(string[6])

# ================СРЕЗЫ - ПОДСТРОКА СТРОКИ========================
# string = 'hello world'
# print(string[0:5])
# print(string[:])

# string[start:end:step]
# print(string[:0:5] [2:4] [:1])
# string[0:5] hello[2:4] ll[0:1]
# print(string[::-1])
# dlr
# string = 'hello world'


# capitalize() - ПЕРЕВОДИТ ПРЕВУЮ БУКВУ В СТРОКЕ В ВЕРХНР=ИЙ РЕГИСТР
# print('hello'.capitalize())

# endswith(element) - ВЩЗВРАЩАЕТ True eсли строка заканчивается на element
# a = 'hELLO WORLD!'
# print(a.endswith('!'))
# вывод True

# startwith() - вщзвраащет True если строка начинается на element
# a = 'makers'
# print(a.startswith('k',2))


# count(element) - cчмиаеи колво вхождений element в строке
# a = 'eiphone'
# print(a.count())

# len() - считает колво букв

# index()

# a = 'hello'
# print(a.index('l'))

# find()

# a = 'Hello World'
# print(a.find('H'))

# id()
# a = 'hello'
# print(id(a))

# str1 = [1,2,3]
# str2 = [1,2,3]
# print(id(str1))
# print(id(str2))

# join() - принимает в себя список 

# text = 'Milk, Bread Water'
# split = text

# text = 'coder'
# print(f'{text[-1]}{text[1:-1]}{text'[0]}')
# print(text[-1] + text[1:4] + text[0])   
# a = "1.1.1.1"
# print(a.replace('.','[.]'))