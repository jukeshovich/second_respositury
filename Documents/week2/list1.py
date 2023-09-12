# list
# СПИСКТ - ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ, УПОРЯДОЧЕННЫЙ(ХРАНИТ ПОРЯДОК ВСТАВКИ В НЕГО ЭЛЕМЕНТОВ)


# ИТЕРИРУЕМЫЙ ТИП ДАННЫХ

# ИТЕРИРУЕМЫЙ ОБЬЕКТ - ОБЬЕКТ ТОТ ТИП ДАННЫХ КОТОРЫЙ  МОЖЕТ ПРОЙТИСЬ ПО КАЖДОМУ ЭЛЕМЕНТУ(ЦИКЛ FOR)

# list_= []
# list()

# list_ = [1,2,3, 'hello', [0,1,2],{"a":3}] #может хранить изм. и неизм тип данных
# print(list_[1]) #- вытащит 2 
# print(list_[4][0])
# print(list_[-1]['a'])
 
# names = input("Enter names with spaces: ").lower().split()
# quest = input("Enter your name: ").lower()
# if quest in names:
#     print("Yes")
# else:
#     print("No")

# СЩЗДАГИЕ СПИСКА

# my_list = list("hello world")
# print(my_list)
# range(0,10) - создает список чисел от 1 до 10
# RANGE() - ВОЗВРАЩАЕТ ПОСЛЕДОВАТЕЬНОСТЬ ЭЛЕМЕНТОВ
# my_list = list(range(0,10,2))
# print(my_list)

# []
# my_list = [1_000-000]
# print(my_list)

# list4 = [2] * 5
# print(list4)

# МЕТОДДЫ СПИСКА

# list_ = ["string",2,4,5,4]
# del list_[0]
# print(list_)
# list_[0] = 1
# print(list_)

# APPEND - ДОБАВЛЯЕТ ЭЛЕМЕНТ В КОНЕЦ СПИСКА
# ПРИНИМАЕТ В СЕБЯ ТОЛЬКО ЭЛЕМИЕНТ
# list = []



# EXTEND - РАСШИРЯЕТ СПИСОК ДОБАВЛЯЯ В  КРНЕЦ ЭЛЕМЕНТЫ

# list_ = [1,5]
# list_.extend("hello")
# print(list_)

# list1 = [1,2,3,4,5]
# list.append([1,2,3])
# list2 = [1,2,3,4]
# list2.extend[1,2,3,4]
# print(list1, list2)

# insert(index, element) ДОБАВЛЯЕТ ЭЛЕМЕНТ ПО УКАЗАННОМУ ИНДЕКСУ

# list1= [1,2,3]
# list1.insert(0,'hello')
# print(list1)

    # INDEX(ELEMENT,START,END) - ВОЗВРАЩАЕТ ИНДЕКС ЭЛЕМЕНТА
# list1 = [1,2,3,4,5,6,2]
# result = list1.index(2)
# print(result)

# CLEAR - ОЧИЩАЕТ СПИСОК

# list1 = [1,2,3,4,5,6]
# print(list1.clear())

# COUNT - СЧИТАЕТ КОЛВО ПРИНЯТОГО ЭЛЕМЕНТА В СПИСКЕ

# list1 = ['hello',1,2,3,4,1,2,3,4,1,23,4,]
# print(list1.count('hello'))

# len - считает длину обьекта
# list1 = [1,2,[1,2,3],3,4]
# print(len(list1))

# POP - УДАЛЯЕТ ЭЛЕМЕНТ ПО ИНДЕКСУ И ВОЗВРАЩАЕТ ЕГО 
# ЕСЛИ ИНДЕКС НЕ УКАЗАН, ТО УДАЛЯЕТ ПОСЛЕДНИЙ ЭЛЕМЕНТ


# list1 = [1,2,3,4,5,6,7]
# popped = list1.pop()
# print(list1)
# print(popped)

#remove удаляет по значению и не возвращает его


# list1 = [1,2,3,4,5,6,7]
# removed = list1.remove(7)
# print(list1)
# print(removed)

# reverse - изменяет список расставляя его элементы в обратном порядке

# list1 = [1,2,3,4,5]
# list1.reverse()
# print(list1)
# print(list1[::-1])

# sort - сортирует список состоящий из элементов одного типа данных в возрастающем порядке(в алфавитном для строк)
# если указан reverse = True то мписок будет отфильтрован в убывающем порядке

# list1 = [1,2,3,3,5,1,55,66,5,1,2,3,4,3,2,1]
# list1.sort(reverse = True) # по умолчанию стоит False в reverse
# print(list1)

# если мы сортируем то список должен иметь одинаковый список данных
# list1 = ['a','f','e','t','f','e','q','d']
# list1.sort()
# print(list1)
# COPY() - КОПИРУЕТ ЛИСТЫ
# list1 = [1,2,3,4,5,[1,2,3,4]]
# list2 = list1.copy()
# print(list2 list1)

# list1 = [1,2,3,4,5,'a','b','c']
# list_num = []
# list_str = []
# for i in list1:
#     if type(i) == type(""):
#         list1vowels.append(i)
#     else:
#         list_num.append(i)
# print(list_num)
# print(list_str)

# цикл - это блок кода который повторяется несколько раз
# мы исп. цикл в тех случаях, когда нам нужно повторить что нибудь n-ое колво раз

# for - цикл, который работает с итерируемым обьектом(list, tuple, str)

# итерируемый обьект  - обьект по которому можно проходиться, который способен возвращать элемент по одному
# число не итерируемый обьект

# string = "string"
# for i in string:
#     print(i)

# for i in [1,2,3,'sda']:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(10):
#     if i == 2:
#         print(i)

# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             print(5, 'j')

# if i == 2:
#     print(2, 'i')

# дан список чисел. отфильтруйте список так, чтобы были четные и нечетные списки

# list1 = [1,2,3,4,5,6,7,8]
# list2 = []
# list3 = []
# for i in list1:
#     if i %2 == 0:
#         list2.append(i)
#     else:
#         list3.append(i)

# print(list3)
# print(list2)

# ИНКРЕМЕНТ УВЕЛИЧЕНИЕ ЗНАЧЕНИЙ КАОЙ ЛИБО ПЕРЕМЕННОЙ 
# ДТКРЕМЕНТ - 

# a = 0
# a = a + 1
# a += 1 - equal a = a + 1
# print(a)

# #dicrement

# a = 0
# a -= 1
# a = a - 1
# print(a)


# НАЙТИ СУММУ СПИСКА
# list1 = [1,2,3,4,5]
# count = 0

# for element in list1:
#     count += element
# print(count)

# ========================================================================================
# 06.09.2023

# guests = []
# guest_length = int(input('enter number of family: '))
# for i in range(guest_length):
#     guest = input("enter family's name: ")
#     guests.append(guest)
#     print(f' У меня в семье {guests}')
# for i in guests:
#     print('У меня в семье есть', i)

# brand = []
# quantity_of_cars = int(input('Введите количество машин, которые хотите добавить: '))
# for i in range(quantity_of_cars):
#     print(brand)
#     name_of_brand = input('Введите название бренда: ')
#     brand.append(name_of_brand)
# print(brand)

# user1 = ['Toyota', 'Volkswagen']
# user2 = ['Mercedes', 'BMW']
# user1.extend(user2)
# user1.extend(['Ferrari','Tesla'])
# print(user1)

# cars = ['4 Toyota RAV4', '7 MercedesG63', '6 Toyota Land Cruiser', '1 Volkswagen Golf 7', '2 BMW E 60', '5 Tesla Model S', '3 Toyota Prius']
# for i in cars:
#     cars.sort(key = len)
# print(cars)


   