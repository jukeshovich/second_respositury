'''
ФУНКЦИЯ ЭТО ИМЕНОВАННЫЙ БЛОК КОДА, ВЫПОЛНЯЮЩУЮ ОПРЕД ЗАДАЧУ И ВОЗВР РЕЗУЛЬТАТ
ОПРЕД С ПОМОЩЬЮ DEF 
'''
# list1 = ['abc', 1, 2, 3]
# count = 0
# for i in list1:
#     count +=1
#     print(count)

# str1 = 'abcde'
# count = 0
# for i in str1:
#     count +=1
#     print(count)

# def my_len(obj):   #обьект должен быть итерируемым
#     count = 0
#     for i in obj:
#         count+=1
#     print(count)

# str1 = 'abcde'
# list1 = ['abc', 1, 2, 3]

# my_len(str1)
# my_len(list1)
'''
ФУНКЦИЯ - ИМЕНОВАННЫЙ БЛОК КОДА, КОТОРЫЙ ВЫПОЛНЯЕТ 1 ЗАДАЧУ И МОЖЕТ
ПРИНИМАТЬ В СЕБЯ ОБЬЕКТЫ И ВОЗВРАЩАТЬ КАКОЕ ЛИБО ЗНАЧЕНИЕ
ФУНКЦИЮ МОЖНО ВЫЗВАТЬ МНОГО РАЗ, ОБРАЩАЯСЬ ПО ИМЕНИ

def - КЛЮЧЕВОЕ СЛОВО, УКАЗЫВАЕТ ЧТО МЫ ХОТИМ СОЗДАТЬ ФУНКЦИЮ
НАЗВАНИЕ ФУНКЦИИ - ПЕРЕМЕННАЯ, ПОД ЭТИМ ИМЕНЕМ ПИТОН ЗАПОМИНАЕТ НАЗВ ФУНКЦИИ
СКОБКИ() - НУЖНЫ ДЛЯ ТОГО, ЧТОБЫ ФУНКЦИЯ МОГЛА ПРИНИМАТЬ ПАРАМЕТРЫ

СИНТАКСИС

def назв. функции(аргументы):
    принимаем аргументы для работы в теле функции
    тело функции

назв.функции(аргументы)
'''

# def my_summ(x,y):
#     print(x + y)
#     return x + y

# my_summ(5,6)
# my_summ(2,0)
# my_summ('sre','da')

# res = my_summ(5,6)

# return - используется для возвращения результата и на этом моменте функция завершвет свою работу
# return - ключевое слово которая дает понять питону что за этой командой будет 
# какая то инфа которая явл. окончат результатом нашей функции


# def sum_2_num(a,b,c=0):   # то что в скобках назыв. параметры
#     print(a,b,c)

# sum_2_num(5,6,3)             #позиционные аргументы
# sum_2_num(a=1, b=2, c=3)   #именованные аргументы


'''
РАСПАКОВКА
'''
# list1 = list(range(1,11))
# print(list1)


# list1 = [*range(1,11)]
# print(list1)

# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {**dict1}
# list3 = {*dict1}
# print(dict2)
# print(list3)

'''
НЕОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ args kwargs
args - принимает позиционные аргументы. Это tuple
kwargs - принимает именованные аргументы. Это dict
ЭТИ АРГУМЕНТЫ НЕОГРАНИЧЕНЫ
'''

# def two_sum(a,b, *args, **kwargs):
#     # print(a,b)
#     # print(args)
#     # print(kwargs)
#     return a + b + sum(args) + sum(kwargs.values())
# print(two_sum(2,5,3,2,4,5,7,5,4,3,2,1,3,5,first = 100, second = 200))

# def func(a, b=10, *args, **kwargs):
#     print('a', a)
#     print('b', b)
#     print('args  ', args)
#     print('kwargs --', kwargs)
# func(1,2,3,4,5,7,6,34,s = 23)

# АНОТАЦИЯ = НАШИ ПОМОЩНИКИ. ДЕЛВЮТ КОД БОЛЕЕ ИНФОРМАТИВНЫМ

# num1: int = 10
# str1: str = 'hello'

# def func(a,b:'анотация', c:int) -> float:
#     '''
#     hello world this sum func
#     '''
#     print(a+b+c)
# func(1,2,3)


#НАЙТИ ПОХОЖИЕ СЛОВА КОТОРЫЕ ПОВТОРЯЮТСЯ ЕСЛИ ЕГО ПЕРЕВЕРНУТЬ
# list1 = ['olo','lol','hello']

# def palidrom(words: list) -> list:
#     palidrom1 = []
#     for word in words:
#         if word == word[::-1]:
#             palidrom1.append(word)
#         else:
#             continue
#     return palidrom1
# print(palidrom(list1))


# ДАГ СЛОВАРЬ УДАЛИТЕ ИЗ НЕГО ВСЕ ЭЛЕМЕНТЫ С ПУСТЫМИ ЗНАЧЕНИЯМИ

# a = {'a':1, 'b':2, 'c':None, 'e':3, 'd':None}
# def func(obj:dict) -> dict:
#     rem1 = {}
#     for key, value in obj.items():
#         if value == None:
#             pass
#         else:
#             rem1[key] = value
#     return rem1
# print(func(rem1))

# РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ

# def validate_email(email:str) -> bool:
#     index = email.find('@')
#     domains = ['gmail.com', 'mail.ru']
#     if '@' not in email:
#         raise Exception('Invalid email')
#     elif not email[0:index]:
#         raise Exception('Invalid email')
#     elif email[index+1:] not in domains:
#         raise Exception(f'Invalid email domain{domains}')
#     print('Email is valid and successfully saved')
#     return True


# # email = input('input email: ')
# # validate_email(email)


# def registered(email:str, password1: str, password2:str) -> dict:
#     db_email = None
#     password = None
#     if validate_email(email):
#         db_email=email
#     if password1 != password2:
#         raise Exception('Пароли не совпадают')
#     password = password1
#     msg = 'Вы успешно зарегистрировались'
#     return {'email':email, 'password': password, 'msg': msg}

# email = input('Введите почту: ')
# password1 = input('Введите пароль: ')
# password2 = input('Подтверлите пароль: ')
# print(registered(email=email, password1=password1, password2=password2))

# def add (num1, num2): 
#     return num1 + num2 
#     print(add(2,3))

# def get_string_length(str): 
#     return len(str) 
#     print(get_string_length('hello'))


# def get_type(x,y): 
#     print(f'{type(x)}\n{type(y)}') 
# get_type(5,'s')

# def divide(a,b): 
#     return a/b 
#     print(divide(5, 10)) 

# dict_={1:'a', 2:'b', 3: 'c', 4:'d'} 
# def dictionary(dict_): 
#     for k,v in dict_.items(): 
#         print(k) 
# dictionary(dict_)

# Напишите функцию, которая определяет, является ли заданное число простым. Простое число - это число, которое делится только на себя и на 1.
# a = int(input('enter number: '))
# def func(a):
#     if a % a == 1:
#         return a
# print(a)

# func(a)

# def is_simple(num: int) -> bool:
#     if num <= 1:
#         return False
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter +=1
#     if counter == 2:
#         return True
#     return False

# print(is_simple(3))
# print(is_simple(10))


# a = [1,4,6,2,1,3,6,8,2,6,7]

# def func(list_: list) -> list:
#     list_ = list(set(list_))
#     list_.sort(reverse=True)
#     return list_

# print(func(a))





# def printsumm(number):
#     summ = 0
#     for digit in str(number):
#         summ+=int(digit)
#     return summ

# number=int(input("Введите число: "))

# print(printsumm(number))

# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно. 
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# num1 = int(input('Enber number: '))
# num2 = int(input('Enter number2: '))
# def sum_range(start:int,end:int):
#     summ = 0
#     if start<end:
#         for i in range(start,end + 1):
#             summ+=i
#     else:
#         for i in range(end,start + 1):
#             summ+=i
#     return summ

# print(sum_range(num1,num2))        


# def sum_range(start:int,end:int):
#     if start > end:
#         start, end = end, start
#     return sum([i for i in range(start, end +1)])
# res = sum_range(num1, num2)
# print(res)

# Напишите функцию, которая принимает число и возвращает список всех его делителей.

# def get_sum(num: int) -> list:
#     list1 = []

#     for i in range(1, num//2):
#         if num % i == 0:
#             list1.append(i)

#     return list1

# print(get_sum(1098))

# def get_sum(num: int) -> list:
#     list1 = [i for i in range(1, num // 2 + 1)if num % i == 0]
#     list1.append(num)
#     return list1
# print(get_sum(10))

# =====================================================================================================
#  CRUD 
# CREATE
# READ 
# UPDATE
# DELETE

import datetime

# database
data = [
{
    'id': 1,
    'name': 'Iphone 14',
    'price': 80000,
    'created_at': datetime.datetime(2022, 9, 4),
    'is_active': True
},
{
    'id': 2,
    'name': 'Iphone 13',
    'price': 70000,
    'created_at': datetime.datetime(2021, 1, 2),
    'is_active': True
},
{
    'id': 3,
    'name': 'Iphone 12',
    'price': 60000,
    'created_at': datetime.datetime(2020, 3, 4),
    'is_active': False
}
]

def get_all():
    return data

# print(get_all())


def get_one(id):                                            # finding some product
    product = [i for i in data if i['id'] == id]
    print(product)
    if product:
        return product
    return 'No such product'
# print(get_one(id))

def post_product():                                         #creating new product
    max_id = max([i['id'] for i in data])
    new_data = {
        'id': max_id + 1,
        'name': input('Name: '),
        'price': int(input('Enter your price: ')),
        'created_at': datetime.datetime.now(),
        'is_active': True
    }
    data.append(new_data)
    return '201 CREATED', new_data

# print(post_product())

def patch_product(id):                                               # changing some product and product will be in last index
    product = [i for i in data if i ['id'] == id]
    if product:
        data.extend(product[0])
        name = input('Name: ')
        price = input('Price: ')
        created_at = input('')
        is_active = input('')
        product[0]['name'] = name
        product[0]['price'] = price
        product[0]['created_at'] = datetime.datetime.now()
        product[0]['is_active'] = True
        data.append(product[0])
        return 'Succesfully changed'
    else:
        return '404', 'You enter wrong number', data
# print(patch_product(2))


def delete_product(id):                                                   # delete some product
    product  = [i for i in data if i ['id'] == id]
    if product:
        data.remove(product[0])
        return 'Succesfully deleted'
    else:
        return 'No such product'
# print(delete_product(2))

# print(data)

# ======================================================================================================================

def main():
    print('Hello, you have acces function: \n\t\t\t\tGET\n\t\t\t\tPOST\n\t\t\t\tDETAIL\n\t\t\t\tPUT\n\t\t\t\tDELETE')
    method = input('Enter one of the function: ').upper()

    if method == 'GET':
        print(get_all())
    
    elif method =='DETAIL':
        id = int(input('Enter ID: '))
        print(get_one(id))

    elif method =='POST':
        print(post_product())

    elif method == 'PUT':
        id == int(input('Enter ID: '))
        print(patch_product(id))
    
    elif method == 'DELETE':
        id == int(input('Enter ID: '))
        print(delete_product(id))

main()




