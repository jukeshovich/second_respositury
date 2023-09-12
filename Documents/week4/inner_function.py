# lambda -функции которые не имеюь названия(анонимная функция) 

# lambda param: что функция возвращает

# def add_nums(a,b):
#     return a + b

# print(add_nums(5,2))

# result = lambda a,b: a + b   # это лямбда функция

# print(result(5,2))

# x = lambda a,b,c: (a*b)%c
# print(x(5,7,10))

# get_keys = lambda x: x.keys()  #если хотим вытащить ключи из словаря
# dict_ = {1:2, 3:4, 5:6}
# print(get_keys(dict_))

# square = lambda a: a**2
# print(square(5))

# get_last = lambda a: ls[0:3] если хотим вытащить элементы из списка
# ls = [1,2,3,4,5]
# print(get_last(ls))

# map(function, iterables) - фукция, принимающ. функцию и итерируемый обьект
# Она применяет функцию к каждому элементу в iterable

# map_gen = map(int,['1','2','3'])
# print(tuple(map_gen))

# nums = [1,2,3,4,5,6]

# def square(number):
#     return number*number

# map_function = tuple(map(square, nums))
# print(map_function)

# list_ = [1, 3,4,5,6,-1,-345]

# list2 = list(map(lambda x: x < 0, list_))
# print(list2)

# func = lambda e: e+1
# res = []
# for e in [1,2,3,4,5]:
#     res.append(func(e))
# print(res)

# filter(function, iterable) - функция принимает первым аргументом другую функцию и 
# итерируемый обьект. Результатом будет последовательность, которая соответствует и прошли условие filter

# nums = [1,2,3,4,5,6,7,8,9,10]

# def filter_nums(number):
#     if number %2 == 0:
#         return True

# result = list(filter(filter_nums, nums))
# print(result)

# nums = [1,2,3,4,5,6,7,8,9,10]

# filter_nums = lambda nums: nums %2 == 0
# print(list(filter(filter_nums,nums)))

# nums = [1,2,3,4,5,6,7,8,9,10]

# res = list(filter(lambda num: num %2 == 0, nums))
# print(res)

# list_name = ['anara','erlan','barsbek','temirlan','kanykei']

# def startwith_vowels(name):
#     vowels = 'aeyuio'
#     print(tuple(vowels))
#     return name.upper().startswith(tuple(vowels))
# print(startwith_vowels('anara'))

# res = list(filter(startwith_vowels, list))
# print(res)

# fiter - работает только по бклевому значению

# res = list(filter(lambda x: if x ))


# list_ = ['Эрлан', 'Атай']
# def startwith_vowels(name):
#     vowels = 'УЕЫАОЭЯИЮ'
#     # print(tuple(vowels))
#     return name.upper().startswith(tuple(vowels))
# res = []

# for name in list_:
#     if startwith_vowels(name):
#         res.append(name)
# print(res)


# reduce - Эта функция принимающая функцию и возвращающая 1 результат
# Его убрали из стандартной библиотеки в ПИТОНЕ, тк ей нашли замену(sum, max)

# from functools import reduce

# list_ = [1,2,3,4,5]
# result = reduce(lambda x, y: x + y, list_)
# print(result)


# from functools import reduce

# list_ = [1,2,3,4,5]

# def mul(a,b):
#     return a*b 
# res = reduce(mul, list_)
# print(res)

# from functools import reduce

# list_ = ['a','s','s','e','w']
# result = reduce(lambda x, y: x + y, list_)
# print(result)


# enumerate(iterable, [start - с какого начинать элементы по дефолту 0]) - ОНа принимает последовательгность. Возвращает tuple 
# состоящий из числа[index] и элемента. return (index,'element')


# list1 = ['a','b','c','d']

# for i in enumerate(list1):
#     print(i)

# list1 = ['a','b','c','d']

# for i in enumerate(list1[1:]):
#     print(i)

# list1 = ['a','b','c','d']

# for i in enumerate(list1,10):
#     print(i)


# list1 = ['one','two','three']
# res = list(enumerate(list1,1))
# print(res)


# zip(iterable, iterable, iterable...) - сопостоавляет каждый элемент из iterable со следующим
# list1 = [1,2,3,4,5,6]
# list2 = ['a','b','c','d','e','F']
# list3 = [1,3,4,6,8,10]
# print(list(zip(list1, list2, list3)))

# any(iterable) - возвращает True ели хотя бы 1 элемент в iterable имеет знач. True

# my_list = [False, True, False, False]
# print(any(my_list))

# all(iterable) - возвращает True если все элементы явл. True

# my_list = [ True, True, True]
# print(all(my_list))

# '''изменить тип данных значений'''

# dict_ = {1: 2, 3: 4, 5: 6}
# map_gen = map(int, dict_.values())
# print(list(map_gen))

# dict_ = {1: 2, 3: 4, 5: 6}
# res = list(map(lambda x: str(x), dict_values()))
# print(res)

# """задача при помощи map() заменить значение чисел словами четное.нечетное"""
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = list(map(lambda x: 'четное' if x % 2 == 0 else 'нечетное', lst))
# print(result)


# def func():
#     for i in lst:
#         if i%2 ==0:
#             print('нечтное')
#         else:
#             print('четное')


# print(res)


# list_ = [1, 5, -9, 6, -4] 
# new_list = all(x > 3 for x in list_)
# print(new_list)



# ============================================================================
'''
встроенные функции - сокращают код и дают нам возможность написать код 
в одну строку и они работают быстрее
'''
'''
Функция map() принимает два аргументы - функция и итерируемый обьект

example
'''
# numbers_str = ['1','2','3','4']
# numbers_int = list(map(int, numbers_str))
# print(numbers_int)

'''
lambda анонимная функция. Является однострочным выражением и не имеет названия
используем ее, когда нам не надо вызывать ее много раз
'''
# numbers = [1,2,3,4]
# double_numbers = list(map(lambda x: x*2, numbers))
# print(double_numbers)
'''
filter() - отвечает за фильтрацию итерируемого обьекта.
Принимает два аргумента - функция и итерируемый обьект, который нужно отфильтровать
Оставляет в итерируемом обьекте только те элементы, для которых функция,
переданная первым аргументом возвращает истину True
'''
# strings = ['Makers','MAKERS','BOOTCAMP','bootcamp']
# upper_string = list(filter(lambda word: word.isupper(), strings))
# print(upper_string)

# numbers = [1,2,3,4,5,6]
# ifer = list(filter(lambda x: x > 4, numbers))
# print(ifer)

'''
reduce - функция которая имеет функцию и итерируемый обьект
складывает итерируемый обьект по очереди
'''

# map(func, iterable object)

# list_str = ['1','2','3','4']
# list_int = []

# for i in list_str:
#     list_int.append(int(i))

# print(list_int)
# это долгий процесс написания кода

# list_str = ['1','2','3','4']
# list_int = list(map(int, list_str))
# print(list_int)
# это простой способ

# def capital(word: str) -> str:     #это называется аннотация типов
#     return word.title()

# list_names =  ['erlan','anara']
# new_list = list(map(capital, list_names))
# print(new_list)

# def integer(x: int) -> int:
#     return x.isalpha()

# def dollars_to_soms(dollars: int) -> int:
#     return f'{round(dollars * 87.80)} soms'

# dollars = [100,50,25,90,65]
# soms = list(map(dollars_to_soms, dollars))
# print(soms)

# print((lambda x: x**2) (46)) #first variant
# square  = lambda x: x ** 2   #second variant
# print(square(48))

# print((lambda x,y,z: x + y + z) (1, 2, 3))

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = [7,8,9]

# new_list = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
# print(new_list)                                         # output [5, 7, 9]

# loop 
# num_list = [3,5,7,54,23,13,43]
# num_list2 = []
# for i in num_list:
#     num_list2.append(i*2)
# print(num_list2)


# list comprehension
# num_list = [3,5,7,54,23,13,43]
# num_list2 = [i*2 for i in num_list]
# print(num_list2)


# map + lambda 
# num_list = [3,5,7,54,23,13,43]
# num_list2 = list(map(lambda i: i*2, num_list))
# print(num_list2)


# filter 
# names = ['erlan','anara','barsbek','temirlan','kanykei']
# filtered_names = list(filter(lambda endname: endname.endswith('n'), names))
# print(filtered_names)

# names = ['erlan','anara','barsbek','temirlan','kanykei']
# start = filter(lambda name: name.startswith('a'), names)
# print(start)

# numbers = [4,5,6,7,8,32,34,5,23, 12]
# filtered_num = list(filter(lambda x: x % 3 == 0, numbers))
# print(filtered_num)

# dict1 = [{'subject':'Python', 'point':69},
#          {'subject':'JS', 'point':92}]
# dict2 = list(filter(lambda x: x['subject'] == 'python'), dict1)
# print(dict2)


print(10/3)
























