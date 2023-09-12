# # a = 'Hello '
# # b = 'World'
# # print(a + b)

# # print('\tHello \nWorld!')

# # a = 'Hello Erlan '
# # print(a*4)

# # name = input('ВВЕДИТЕ ВАШЕ ИМЯ: ')
# # result = "Hello %s" %name
# # print(result)

# # str = 'Python'
# # print('Hello Python developers! Welcome to, %s!' %str)

# # name = input('Enter your name: ')
# # print("Hello, mr %s " %name)
# # print("WElcome to our Website")

# # my_name = 'Erlan'
# # your_name = 'Anara'
# # name_of_sun = 'Barsbek'
# # result = 'Hello {1},{2},{0}'.format(your_name, my_name, name_of_sun)
# # print(result)

# # car1 = 'Toyota'
# # car2 = 'Mercedes'
# # car3 = 'VW'
# # result = 'My cars are {}, {} and {}'.format(car1, car2, car3)
# # print(result)

# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# result = f'Hello, {name}. Welcome to our website. You are {age} years old.'
# print(result)

# string = '1234'
# print(string.isalpha())

# a = 'asd'
# print(a.isalpha())

# a = 'weqd32'
# print(a.isalnum())

# a = 'dAsa12'
# print(a.islower())

# a = "    "
# print(a.isspace())

# a = 'Erlan'
# print(a.istitle())

# a = 'eRLAN'
# print(a.swapcase())

# a = 'ANARA'
# print(a.title())

# a = '  Erlan  '
# print(a.strip())

# a = "   ERLAN   "
# print(a.rstrip())

# a = 'Hello, my name is Erlan'
# print(a.replace('Hello', 'Good morning'))

# a = 'Hello, Hello, Hello'
# print(a.replace('Hello', 'Good morning', 2))

# a = 'ErlanAnara'
# print(a.split(',')) &&&

# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# result = f'Hello, {name}. Welcome to our website. You are {age} years old.'
# print(result)

# name = input('Введите ваше имя: ')
# last_name = input('Введите вашу фамилию: ')
# age = int(input('Введите ваш возраст: '))
# city = input('Введите ваш город: ')
# result = f'Вас зовут {name} {last_name}, Ваш возраст: {age} лет, Вы проживаете в городе{city}'

# print(result)

# a = 'Hello, my, dear,World'
# print(a.split("e"))

# 18/08/2023

# a = 3
# str(a)
# print(a)
# name = "Erlan"
# for letter in name:
#     print(letter)
# ЦИКЛ FOR ПОЗВОЛЯЕТ ПРОЙТИСЬ ПО КАЖДОМУ ЭЛЕМЕНТУ ИНТЕРИРУЕМОГО ОБЬЕКТА
# другой пример
# name = "Erlan"
# for letter in name:
#     pass

# =======================УСЛОВНЫЕ ОПЕРАТОРЫ===================
# money = 100
# if money > 100:
#     print("buy kefir")
# elif money == 0:
#     print("go to work")
# else:
#     print("buy banana") 

# str_ = "    erlan  erkab   "+
# new_str = str_.replace(" ", '')
# print(new_str)
'''
вычислить сколько преедложений в переменной
'''

# text = "John snow is very smart. He likes banana. He loves Maria. He's married."
# counter = text.count(".")
# print(counter)

# name = "sfeeeeeeeee sfeeeeeeeeeee fseefsfsfessffs. fsfefs"
# name1 = name.replace(" ", '')
# name2 = name.split()
# print(name2)

# name = "erlAN. ERLAN. RLAN. LAM."
# name1 = name.replace(". ", "")
# print(name1) 

full_name = input("Введите ФИО: ")
full_name_list = full_name.split()
result = full_name_list[0].capitalize() + ' ' + full_name_list[1][0].capitalize() + ' ' + full_name_list[2][0].capitalize()
print(result)
# full_name = input("Введите ФИО: ").title().split()
# res1 = f'{full_name[0]} {full_name[1][0]} {full_name[2][0]}'
# print(res1)

# name = input()
# if "сок" in name:
#     print("true")
# else:
#     print('false')


