# множества и кортежи

# что такое множество 
# синтаксис и основные свойства множеств
# что такое кортеж, основные свойства кортежа
# цикл while

# множества(set)  - изменяемый тип данных, который представяет собой
# неупорядоченную коллекцию уникальных элементов. 
# ОНИ изменяемы, неупорядоченны и уникальны

# МНОЖЕСТВА SET МОЖНО СОЗДАТЬ НЕСКОЛЬКИМИ МЕТОДАМИ. 
# САМЫЙ ПРОСТОЙ ИЗ НИХ ЭТО ЗАДАТЬ МНОЖЕСТВО ПУТЕМ ПЕРЕЧИСЛЕНИЯ
# ЕГО ЭЛЕМЕНТОВ ВНУТРИ ФИГУРНЫХ СКОБОК.

# set1 = {1,2,3}
# print(type(set1))

# ОДНАКО НЕЛЬЗЯ СОЗДАВАТЬ ПУСТОЕ СНОЖЕСТВО, ТАК КАК ОНО СОЗДАСТ
# ПУСТОЙ СЛОВАРЬ

# set1 = {}
# print(type(set1))

# А ЧТОБЫ СОЗДАТЬ ПУСТОЕ МНОЖЕСТВО НЕОБХОДИМО ИСПОЛЬЗОВАТЬ
# ФУНКЦИЮ SET 

# set1 = set()
# print(type(set1))

# свойства множеств
# неупорядоченны. Порядок расположения элементов в множестве
# не имеет значения. А это значит, они не индексируются и не поддерживают 
# операции срезов или же получения индекса по срезу

# изменяемость.
# множества изменяемы и поддердживают 
# обьединение множеств
# добавление элементов
# удаление элементов

# УНИКАЛЬНОСТЬ
# МНОЖЕСТВА ДОЛЖНЫ БЫТЬ УНИКАЛЬНЫМИ А ЭТО ЗНАЧИТ ОНО НЕ МОДЕТ СОДЕРЖАТЬ 
# ОДИНАКОВЫХ ЭЛЕМЕНТОВ

# САМО ПО СЕБЕ МНОЖЕСТВО НЕИЗМЕНЯМЫ И ЕГО МОЖНО МЕНЯТЬ.
# ОДНАКО ЭЛЕМЕНТЫ МНОЖЕСТВА ЯВЛЯЮТСЯ НЕИЗМЕННЫМИ, ОТНОСЯТСЯ
# К НЕИЗМЕНЯЕМЫМ ТИПАМ ДАННЫХ

# ГДЕ ИСПОЛЬЗУЮТСЯ МНОЖЕСТВА
# ЕСЛИ НАМ НУЖНО ПОЛУЧИТЬ УНИКАЛЬНОЕ ЗНАЧЕНИЕ КОТОРОЕ НЕ ПОВТОРЯЕТСЯ

# МЕЖДУ МНОЖЕСТВАМИ МОГУТ БЫТЬ НЕСКОЛЬКО СВЯЗЕЙ ИЛИ ОТНОШЕНИЙ
# 1. РАВНЫЕ МНОЖЕСТВА. 
# ТАК НАЗЫВАЮТСЯ ПОТОМУ ЧТО МОГУТ ИМЕТЬ ДВА МНОЖЕСТВА С 
# ОДИНАКОВЫМИ ЭЛЕМЕНТАМИ
# 2. НЕПЕРСЕКАЮЩИЕСЯ МНОЖЕСТВА
# ТАК ГОВОРЯТ КОГДА МНОЖЕСТВА НЕ ИМЕЮТ ОДИНАКОВЫХ ЭЛЕМЕНТОВ
# 3. ПОДМНОЖЕСТВА И НАДМНОЖЕСТВА

# В ЯЗЫКЕ ПАЙТОН СУЩЕСТВУЮЕТ ТИП ДАННЫХ
# С ХАРАКТЕРИСТИКАМИ МНОЖЕСТВА
# НО С НЕБОЛЬШИМ ОТЛИЧИЕМ А ИМЕННО СВОЙСТВОМ НЕИЗМЕНЯЕМОСТИ
# ТАКОЙ ТИП ДАННЫХ НАЗЫВ. ЗАМОРОЖЕННОЕ МНОЖЕСТВО ИЛИ frozenset
# frozenset - НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ С ХАРАКТЕРИСТИКАМИ МНОЖЕСТВА
# ЗАЧЕМ НАМ НУЖЕН FROZENSET
# ЭТОТ ТИП ДАННЫХ ИСП НЕ ТАК ЧАСТО ВМЕСТО НЕГО ИСПОЛЬЗУЮТ КОРТЕЖ

# TUPLE = УПОРЯДОЧЕННЫЙ ТИП ДАННЫХ КОТОРЫЙ НЕИЗМЕНЯЕТСЯ И ПРЕДСТАВЛЯЕТ 
# ПОСЛЕДОВАТЕЛЬНОСТЬ ЭЛЕМЕНТОВ
  
# ЦИКЛ WHILE  ПОКА 
# ЭТО УНИВЕРСАЛЬНЫЙ ЦИКЛ ЕГО СИНТАКСИС ИДЕТ ТАК

# while True_or_False_expression:
#     do_something

# похож на оператор if

# В while  ПОТОК ВОЗВРАЩАЕТСЯ К ЗАГОЛОВКУ ЦИКЛА И СНОВА ПРОВЕРЯЕТ 
# УСЛОВИЕ. ЕСДИ ЛОГИЧЕСКОЕ ВЫРАЖЕНИЕ ВОЗВРАЩАЕТ True ТО ЦИКЛ
# СНОВА ВЫПОЛНЯЕТСЯ ДО ТЕХ ПОР ПОКА ЛОГИЧЕСКОЕ ВЫРАЖЕНИЕ НЕ ВЫДАСТ False

# с циклом используются опервторы break и continue
# break ДАЕТ ВОЗМОЖНОСТЬ ВЫЙТИ ИЗ ЦИКЛА ПРИ СРАБАТЫВАНИИ 
# ВНЕШНЕГО УСЛОВИЯ
# ПОМЕЩАЕМ ОПРЕТОР BREAK ПОД ОПЕРВТОРОМ WHILE.
# ОБЫЧНО ПОСЛЕ УСЛОВНОГО ОПЕРВТОРА IF
# И ОПЕРАТОР BREAK ПРИВОДИТ К ВЫХОДУ ИЛИ РАЗРЫВУ ИЗ ЦИКЛА

# ОПЕРАТОР CONTINUE
# ДАЕТ ВОЗМОЖНОСТЬ ПРОПУСТИТЬ ЧАСТЬ ЦИКЛА В КОТОРЫЙ СРАБАТЫВАЕТ 
# ВНЕШНИЕ УСЛОВИЯ НО ПОЗВОЛЯЕТ ПРОДОЛЖИТЬ ВЫПОЛНЕНИЯ ЦИКЛА ДО КОНЦА


# empty = set()
# print(type(empty))

# a = {'makers', 4, 9, True, False}
# b = set('makers')
# print(a)
# c = set(range(1,10,2))
# print(c)

# set1 = {'hello', 2, True, [1,2,3]}
# print(set1)

# СПИСОК, СЛОВАРЬИ САМО МНОЖЕСТВО НЕ МОЖЕТ БЫТЬ ВНУТРИ МНОЖЕСТВА ТАК КАК ОНИ ТАКЖЕ ЯВЛЯЮТСЯ
# ИЗМЕНЯЕМЫМИ

# СРАНЕНИЕ МНОЖЕСТВ
# set1 = {1,5,3,9,8}
# set2 = {9,1,5,3,8}
# set3 = {1,5,1,3,3,8,8,8,9,9}
# print(set1 == set2)
# print(set3)
# print(set3 == set2)

# set1 = {1, 1.0, True}   что было вначале то и выводит так как они все равны
# print(set1)

# set3 = {1,5,1,3,3,8,8,8,9,9}   
# print(len(set3))               дает только колво уникальных элементов работает также и со строками

                                            # ==================МЕТОДЫ==========
# add()

# quests = {'Tom', 'Sam', 'John', 'Emily'}
# print(quests)
# quests.add('Rachel')
# print(quests)

# update() перезагружает множество с новыми элементами из другого множества
# при этом повторяющиеся элементы не обновляются

# set1 = {1,2,3}
# set2 = {3,5,4}
# set1.update(set2)
# print(set1)

# remove(), discard(),
# pop()- УДАЛЯЕТ СЛУЧАЙНЫЙ ЭЛЕМЕНТ
# clear() - ОЧИЩАЕТ МНОЖЕСТВО

# quests = {'a','b','c'}
# quests.discard('a')
# # print(quests)

# quests.pop()
# print(quests)

# copy() создает копию

# quests = {'Tom', 'Sam', 'John', 'Emily'}
# quests2 = quests.copy()
# quests.add('Rachel')
# print(quests)
# print(quests2)

# intersecection() находит пересечение двух множеств. неизменяет множество 
# а возвращает нам множества пересек. элементов с другим множеством
# & ampersand(аналог и)
# music_students = {"Sam", "Alice", "Kate",
#                    "Ben", 'John',}
# art_students = {'Rachel', 'Sam', 'John',
#                 'Catherin'}
# it_students = {'Sam', 'Tom'}
# print(music_students & art_students & it_students)

# union() обьединяет оба множества без повторяющихся элементов
# | тот же метод
# music_students = {"Sam", "Alice", "Kate",
#                    "Ben", 'John',}
# art_students = {'Rachel', 'Sam', 'John',
#                 'Catherin'}
# print(art_students | music_students)

# difference() минусует из одного множества другое множемвто. Если в обоиз множемтвах есть похожие элементы 
# он их отбрасывает и выводит только уникальные элементы
# -(минус) тот же метод
# music_students = {"Sam", "Alice", "Kate",
#                    "Ben", 'John',}
# art_students = {'Rachel', 'Sam', 'John',
#                 'Catherin'}
# print(music_students.difference(art_students))

# symmetric_difference() возвращает нам уникальные в двух множествах элементы
# а похожие отбрасывает

# music_students = {'Sam', 'Alice', 'Kate',
#                    'Ben', 'John',}
# art_students = {'Rachel', 'Sam', 'John',
#                 'Catherin'}
# res = music_students.symmetric_difference(art_students)
# print(res)

# isdisjoint() - возвращаает TRue или False 
# Если в двух множествах есть не похожие элементы, то выходит True
# если есть похожие то False 

# num1 = {1,2,3,4}
# num2 = {5,6,7}
# print(num1.isdisjoint(num2))

# issuperset(), issubset() - Данные методы возвр. True or False 
# в тех случаях когда множества явл. надмножествами или подмножетсвами

# a = {1,2,3,4,5,6}
# b = {3,5}
# print(b.issubset(a))

# intersection_update() методы которые меняют наше множество
# изменяет то множество к которому применяется данный метод

# num1 = {1,2,3,4,5}
# num2 = {2,5,1}
# num1.intersection_update(num2)
# print(num1)

# difference_update() - # изменяет то множество к которому применяется данный метод

# num1 = {1,2,3,4,5,6}
# num2 = {5,2,7,8}
# num2.difference_update(num1)
# print(num2)

# symmetric_difference_update() возвращает не пересекающиеся элементы

# num1 = {1,2,3,4,5}
# num2 = {6,9,0,2,4}
# num1.symmetric_difference_update(num2)
# print(num1)

# frozenset такое же множество но неизменяемое, то есть не можем 
# добавить ил удалить или поменять. И оно не часто используется

# frozen = frozenset('makers')
# print(frozen)

 
# 24.08.23

# set() - множества. Это измнгяемый тип данных, неупорядоченный, итерируемый, неиндексируемый и и хранит уникальные ключи.
# Хранят только неизменяемые типы двнных

# set1 = set()
# set2 = {} - так создаются слловари
# set = {1,2,3,4}
# print(set)

# set3 = {True, 0, 1, False }
# print(set3)

# a = set([1,2,3,4,5]) #так надо писать когда исп. через set()
# print(a)

# b = set({1:"1", 2:"2"}) #- раюотает  поьому что ключи в словаре неизменяемы
# print(b)

# c = set('Hello world!') 
# print(c)  

# set1 = {1,2,3,(1,2,3),'s'} - ЕСЛИ ДАЖЕ В КОРТЕЖЕ ЕСТЬ СПИСОК ТО ВСЕ РАВНО НЕ СРАБОТАЕТ
# print(set1)

# add() - добавление элементов

# set1 = {1,2,3,4}
# set1.add{3}
# set1.add('hello') # во мнодество нельзя добваить другое мноедство 
# print(set1)

# update() - обновление элементов
# set1 = {1,2}
# set1.update([1,2,3,4,5])
# set1.update({6:'1', 2:'2'})
# set1.update('string',[1,2,3,4,5,6,7])
# print(set1)

# Удаление элементов

# clear() -очищает множество

# remove() - удаляет элемент, если элемента нету то выдаеи ошибку

# set1 = {1,2}
# set1.remove(2)
# print(set1)

# discard() - удаляет элемент, но если элемента нет, то ничего не происходит
# set1 = {1,2,3}
# set1.discard(4)
# print(set1)

# pop() - удаляет случайный элемент из set(0) и возвращает

# set1 = {1,2,3,4}
# popped = set1.pop()
# print(set1)

# difference - выводит элементы которые есть в set1 но нет в set2
# - то же значение
# set1.difference(set2)

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 - set2) ----> {1,2}
# print(set1.difference(set2)) ---->{1,2}

# symmetric_difference() -  выводит элементы которые уникальны в обоих сетах
# set1^set2

# set1 = {1,2,3,4}
# set2 = {5,6,7,8,3}
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# intersection() - выводит походие элементы из set1 и set2
# set1 & set2

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 & set2)
# print(set1.intersection(set2))

# union() - соединяет множества
# |

# a = {1,2}
# b = {3,4}
# print(a|b)
# print(a.union(b))

# set1 = {1,2,3,4}
# list1 = (5,6,7,8)
# res = set1.union(list1)   #- может работать с другими типами данных (кортежи и списки)
# print(res)


# цикл while

# ЦИКЛ - БЛОК КОДА, КОТОРЫЙ ПОВТОРЯЕТСЯ ОПРЕДЕЛЕННОЕ УОЛВО РАЗ
# ИЛИ РАБОТАЕТ БЕСКОНЕЧНО

# for - цикл, который работает с итерируемыми обьектами
# и закончит свою работу на последнем элементе

# while - цикл, который работает пока условие верно
# while - пока Парвда
# после while идет условие цикла и пока это условие верно, то цикл будет работать
# остановить цикл можно комбинацией ctrl+c или ctrl+z

# counter = 0
# while True:
#     counter += 1
#     print(counter)

# count = 0
# while count != 100:  #---- пока count не равен 101
#     print(count)
#     count +=1
# print('end')

# count = 10
# while count != 0:
#     print(count)
#     # count -= 1
#     count = count - 1
# print('end')

# a = 0     # - не работает потому что 0 это False
# while a:
#     print('hello')

# for i in range(1,10):
#     print(i)
# print(i)

# for i in 10:
#     print(i) - int is not itaerable

# num = 12345
# sum = 0
# for i in str(num):
#     sum += int(i)
# print(sum)

# string = 'hello'
# string1 = 'world'
# for i in range(len(string)):
#     print(i, string[i], string1[i]) 

# пример создания бесконечного цикла с помощью for 
# list1 = [1,2,3]
# for i in list1:
#     print(i)

# ключевые слова цикла
# 1. break досрочно прерывает цикл. ПОлнсотью выйти из цикла
# 2. continue - переходит к следующей итерации пропуская элемент


# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
#     if i == 3:
#         continue

# for i in range(10):
#     print(i)
#     if i == 3:
#         break     попробуй print запустить 
#     # print(i)

# i = 0
# while i<6:
#     if i == 3: break
#     else:
#         print(i)
#         i+=1


# for i in range(10):
#     print(i)
#     for j in range(10):   interesting 
#         print(j)
#         if j == 5:
#             break
#     if i == 2:
#         break

# list1 = [1,2,3,4,5,2,3,2,3,2]
# while 2 in list1:
#     list.remove(2)
# print(list1)

# while True:
#     print(1)
#     continue
#     print(2)

# else примененное в цикле for и while проверют, был ли произведен
# выход из цикла с помощью break, или же естественным образом
# else сработает если выход из цикла был совершен без помощи break

# for i  in 'hello world':
#     if i == 'd':
#         break
# else:
#     print('hello world')

# for num in range(5):
#     if num < 3:
#         pass
#     else:
#         print(num)

# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
# for key in dict1:
#     print(key)

#     dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
# for val in dict1.values():
#     print(val)

# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
# for i in dict1:
#     print(i.get())

# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
# for i in deict1.items():
#     key = items[0]
#     value = items[1]
# play = True
# while play:
#     operator = (input("enter operator + - / *: "))
#     num1 = int(input("enter your first number: "))
#     num2 = int(input("enter your second number: "))
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         print(num1 / num2)
#     operator2 = input("Do you want to continue?: Yes or No ").lower()
#     if exit.lower == 'yes':
#         continue 
#     elif exit.lower == 'no':
#         print('bye bye') 
#         play = False
#     else:
#         print('Type Yes or no')

# while True:
#     operator = input("enter operator + - / *: ")
#     num1 = int(input("enter your first number: "))
#     num2 = int(input("enter your second number: "))
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         print(num1 / num2)
#     quest = input('Хотите Продолжить :').lower()
#     if quest == 'да':
#         continue
#     elif quest == ('нет'):
#         print('Пока')
#         break
#     else:
#         print("Укажите 'да' , 'нет' ")

# Попросите студентов написать программу, которая запрашивает у пользователя пароль и проверяет его на соответствие определенным требованиям. Пароль считается валидным, если он:

# Содержит как минимум 8 символов.
# Содержит хотя бы одну заглавную букву.
# Содержит хотя бы одну строчную букву.
# Содержит хотя бы одну цифру.
# Содержит хотя бы один специальный символ (например, !, @, #, $ и т.д.).

# user = input("Введите пароль: ")
# if len(user) < 8:
#     print('Ваш пароль должен содержать не менее 8 символов')
# elif user.capitalize() == False:
#     print('Пароль должен содержать хотя бы одну заглавную букву.')
# elif user.isupper() == True:
#     print('Пароль должен содержать хотя бы одну строчную букву.')
# elif user.isdigit() == False:
#     print('Пароль должен содержать хотя бы одну цифру.')
# else:
#     print('Пароль успещно созранен')


# user = input("Введите пароль: ")
# if len(user) < 8:
#     print('Ваш пароль должен содержать не менее 8 символов')
# elif user.islower() == True:
#     print('Пароль должен содержать хотя бы одну заглавную букву.')
# elif user.isupper() == True:
#     print('Пароль должен содержать хотя бы одну строчную букву.')
# elif user.isalpha() == True:
#     print('Пароль должен содержать хотя бы одну цифру.')
# elif user.isalnum() == True:
#     print('Пароль должен содержать хотя бы один специальный символ (например, !, @, #, $ и т.д.).')
# else:
#     print('Пароль успешно сохранен')

# string = 'makerss' # -> string[4:] + string[:4]
# center  = len(s tring) // 2 # -> 7 // 2 = 3

# center = string[]
# print(center)
# if len(string) %2 == 0:
#     res = string[center:] + string[0:center]
#     print(res)
# elif len(string) %2 == 1:
#     res = string[center+1:] + string[0:center+1]

#     print(res)

x = int(input('Enter1: '))
y = int(input('Enter2: '))
# res = x/y
# res2 = x%y
if x % y == 0:
    print('x делится на y')
    print('Частное: ', int(x/y))
elif x % y == 1:
    print('x не делится на y')
    print('Частное: ', int(x/y))
    print('Остаток: ', int(x%y))
