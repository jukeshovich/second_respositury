# def decor_func(func):
#     print('decor func')
#     return func()

# def func2():
#     print('func2')
#     return 'hello'

# def func3():
#     print('func3')
#     return 'world'

# res = decor_func(func2)
# print(res)
# res1 = decor_func(func3)
# print(res1)


# декоратор - функция которая в свою очередь принимает другую фкнкцию
# Декоратор явл функцией высшего порядка - это функции которые могут принять как аргумент другую функцию и вернуть ее
# Декоратор модифицирует и улучшает принятую функцию и выдает измененную


# def func2(func):
#     print('Я буду работать до фукции func1')
#     print(func())

# def func1():
#     return 'функция func2 завершилась'

# func2(func1)

# def decor_func(func):
#     def wrapper():
#         original_res = func()
#         modified_res = original_res.upper()
#         return modified_res
#     return wrapper

# @decor_func
# def some_text():
#     return 'Hello world'
# @decor_func
# def some_text1():
#     return 'hello KG'


# # res = decor_func(some_text)
# # print(res())

# # res1 = decor_func(some_text1)
# # print(res1())

# print(some_text())
# print(some_text1())


# def get_name(name):
#     return name

# def get_age(age):
#     return age 

# def get_last_name(last_name):
#     return last_name

# print(get_name('Elan'))
# print(get_age(26))
# print(get_last_name('Jukeshovich'))


# def decorator_func(func):
#     def wrapper(some_info):
#         return 'Вы передали: ' + str(func(some_info))
#     return wrapper

# @decorator_func
# def get_name(name):
#     return name

# @decorator_func
# def get_age(age):
#     return age 

# @decorator_func
# def get_last_name(last_name):
#     return last_name

# print(get_name('Elan'))
# print(get_age(26))
# print(get_last_name('Jukeshovich'))

# def func_def(function_to_decorate):     #сюда попадает функция которую нужно задекорировать
#     def wrapper():                      # wrapper - это оберточная оболочка для функции
#         print('Я код который обрабатывает до вызова функции')
#         function_to_decorate()
#         print('А я код который сработает после!!!')
#     return wrapper                       #возвращает обертку

# # @func_def                                # это первый способ вызвать декоратор
# def func1():                             #функция которую иы задекорируем
#     print('Я функция func1')

# res = func_def(func1)                    # это второй способ декорировать 
# res()


# ЕСЛИ МЫ ИСП. АРГУМЕНТЫ У ФУНКЦИИ, ТО МЫ ТАКЖЕ ОБЯЗАТЕЛЬНО ДОЛЖНЫ ПЕРЕДАВАТЬ ИХ В ДЕКОРАТОР

# def decorator(func):
#     def wrapper(arg):
#         print(f'Смотри, что я принимаю {arg}')
#         func(arg)
#     return wrapper

# @decorator
# def func1(word):
#     print(f'Я принимаю в себя слово {word}')

# func1('YES')

# def decorator(func):
#     def wrapper(arg):
#         print(f'просто текст {arg}')
#         func(arg)
#     return wrapper

# @decorator
# def func1(name):
#     print(f'Ich bin {name}')

# func1('ERLAN')


# def decorator(func):     #лучше использовать такую запись, тк она универсальная для всех функции
#     def wrapper(*args, **kwargs):
#         print(f'здесь аргс {args}')
#         print(f'здесь кваргс{kwargs}')
#         func(*args, **kwargs)
#     return wrapper
# @decorator
# def func_without_param():
#     print('функия без параметров')

# @decorator
# def func_with_param(first_name, last_name):
#     print('функция с параметром')
#     print(f'hello {first_name} {last_name}')

# @decorator
# def func_with_param_kwargs(first_name, last_name):
#     print('функция с параметром')
#     print(f'hello {first_name} {last_name}')
    

# func_without_param()
# func_with_param('erlan','jukeshovuch')
# func_with_param_kwargs(first_name = 'erlan',last_name = 'jukeshovuch')

# def div(func):
#     print('f1')
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return '<div>' + func(*args, **kwargs) + '</div>'
#     return wrapper

# @div
# def get(name, last_name):
#     print('f2')
#     return name + last_name

# print(get('Erlan','Snow'))


# def bread(func):
#     def wrapper(*args, **kwargs):
#         return 'bread ' + str(func(*args, **kwargs)) + ' bread'
#     return wrapper

# def ingredients(func):
#     def wrapper(*args, **kwargs):
#         return 'tomato ' + str(func(*args, **kwargs)) + ' salad'
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(x):
#     print(x)
#     return x

# print(get_sandwich('sausage'))


# res = ingredients(get_sandwich('sausage')) #tomato sausage salad
# res1 = bread(res)                          #bread tomato sausage salad bread


# def my_decorator(func):
#     print('Я декоратор. Я буду вызван в момент декорации функции')
#     def wrapper():
#         print('Я функция обертки. Вызываюсь каждый раз при декорировании функции')
#         return func()
#     print('Я возвращаю обернутую функцию')
#     return wrapper

# @my_decorator
# def decorate_function():
#     print('Я декорированная функция')

# decorate_function()

# def decorator_maker(f):
#     print(f)
#     print(f'Я создаю декораторы')
#     def my_decorator(func):
#         print('Я декоратор. Я буду вызван в момент декорации функции')
#         def wrapper():
#             print('Я функция обертки. Вызываюсь каждый раз при декорировании функции')
#             return func()
#         print('Я возвращаю обернутую функцию')
#         return wrapper
#     return my_decorator

# @decorator_maker(2)
# def decorate_function():
#     print('Я декорированная функция')

# decorate_function()


# def banchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'function worked: {end - start}')
#     return wrapper
# @banchmark
# def call_webpage():
#     import requests
#     webpage = requests.get('https://google.com')

# @banchmark
# def iterate_list():
#     for i in range(5000001):
#         print(i)

# # call_webpage()
# iterate_list()



# def summa(a):
#     res = 0
#     for i in str(a):
#         res += int(a)
#     return res

# print(summa(125))


# def func(a,b,c):
    
























