# Области видимости и пространство имен

# пространство имен

# 1) __builtins__(втсроенные имена) - асе что встроено в оболочку питона

# print(dir(__builtins__)) - показывает все встроенные переменные

# 2) global все переменные внутри файла которую мы создали

# a = 5 -это глобальная переменная

# 3) enclosed - пространство находящиеся между двумя пространствами(между global и local)

# 4) local - локальное пространство имен

# по мере выполнения программы ПИТОН создает разные пространства имен и удаляет их

# ========================================================================================
# 1

# a = 10
# b = 'hello'

# print(globals())

# x = 10
# print(globals()['x'])
# print(x is globals()['x'])

# globals - вщзвращает словарь с глобальными переменными

# 2

# def hello():
#     a = 'hello world'
#     print(locals())

# hello()
# # print(locals())  #- нисего не выйдет так как онаходится внутри функции

# def func(b,c):
#     a = 5
#     print(locals())

# func(5,2)
# print(locals()) #- дает все знасения как и globals

# enclosed - она возникает когда есть влоденности в функции

# x = 'глобальная область видимости'

# def func():
#     x = 'это enclosed область видимости'
#     print(x)
#     def func2():
#         x = 'это локальная область видимости'
#         print(x)
#     func2()
# print(x)
# func()

# def func():
#     a = 'Erlan'
#     # encloses
#     def func2():
#         a = 'Anara'
#         # local
#         print(locals())
#     func2()
#     print(locals())
# func()
# print(globals())

# a = 10
# def func():
#     b = 'local'
#     return a + 100

# # print(b)
# print(func())

# порядок поиска переменных
# local -> enclosed -> global -> builtins

# x = 10

# def func():
#     x = 20
#     print(x, 'x is local')
# func()
# print(x, 'x is global')

# def func():
#     global x
#     x = 20
#     print(x, 'x is local')
# func()
# print(x, 'x is global')

# global - позволяет менять значение глобальной переменной, находясь в локальной области видимости

# count = 0

# def counter():
#     print(count)
#     count += 1
# counter()

# count = 0

# def counter():
#     try:
#         print(count)
#         count += 1
#     except:
#         print('f')
# counter()
# counter()

# count = 0

# def counter():
#     global count
#     count += 1
#     print(count)

# counter()
# counter()
# counter()

# def outerFunction():
#     global a
#     a = 20
#     def innerFunction():
#         global a
#         a = 30
#         print('inner function a =', a)
#     innerFunction()
#     print('outer function a =', a)

# a = 10 #20 #30
# outerFunction()


# def func():
#     a = '1'
#     def innerFunc():
#         def innerFunc2():
#             nonlocal a
#             a = 2
#         innerFunc2()
#     innerFunc()
#     print(a)
# func()

# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 'Edited enclosed x'
#         print(x, 'is local')
#     local()
#     print(x, 'is enclosed')
# enclosed()

# def func():
#     var = 100
#     def nested():
#         nonlocal var
#         var += 100
#     nested()
#     print(var)
# func()

# def count(i):
#     counter = 0

#     def add():
#         nonlocal counter
#         print(counter)
#         counter +=1

#     for x in range (i):
#         add()

# count(10)

# обычно nonlocal позволяет нам назначать переменные во внешней области но не в глобальной

# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 30
#         def inner():
#             nonlocal x
#             x = 'Edited x'
#             print(x, 'inner()')
#         inner()
#     local()
#     print(x, 'enclosed')

# enclosed()
















