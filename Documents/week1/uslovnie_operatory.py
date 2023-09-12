# ЛОГИЧЕСКИЕ ОПЕРАТОРЫ

# print(bool(0)) False
# bool(9) True 
# bool(-277) True

# bool('hello') True 
# bool(' ') True
# bool('') False

# != не равно

# print(5 !=5)

# ЛОГИЧЕЧЕСКИЕ ОПЕРАТОРЫ

# and - логическое и
# or - логическое или
# not - логическое отрицание

# a = 5
# b = 6
# print(a== 5 and b ==6) True
# a == 4 and b == 6 - False

# print(a == 5 or b == 7)

# print(not True)
# print(not False)
# not a == 5 - False
# not a ==4 - True

# ОПЕРАТОР ИНДЕНТИФИКАЦИИ

# in проверяет наличие элемента

# сравнение

# == - сравнение по значению
# is - сравнение по ячейкам памяти

# str = "hello"
# if q in str:
#     print("worked")

# a = 2
# b = 2
# print(id(a))
# print(id(b))

# a = [1,2,3]
# b = [1,2,3]
# print(a is b) False
# print(a == b) True

# a = None
# print(a is None) - True

# УСЛОВНЫЕ ОПЕРАТОРЫ НУЖНЫ ДЛЯ ТОГО, ЧТОБЫ ПРИ РАЗНЫЪХ ВХЛДНЫХ ДАННЫХ КОД РАЮОТАЛ ПО РАЗНОМУ

# if условие1:
#     тело1

# if условие1:
#     тело1
#     будет работать усли условие1 верно
# else:
#     тело2
#     будет работать если условие1 не верно

# if условие1:
#     тело1
#     будет работать усли условие1 верно
# elif условие2:
#     тело2
#     будет работать если условие 2 верно
# else:
#     тело2
#     будет работать если условие1 не верно

#  в одной конструкции мы можем использовать только один if
# в одной конструкции мы можем использовать неограниченное колва elif или не использовать вообще
# else мы также можем исп. всего 1 раз


# a = 'Hello'
# if 'h' in a:
#     print('worked')
# if a:
#     print('worked')
# if len(a) > 3:
#     print('worked')

# user = int(input())
# if user >= 18:
#     print("ok")
# else:
#     print("not ok")

# user = int(input())
# if user >= 18:
#     print("ok")
# else:
#     print("not ok")

# import random
# res = random.randint(1,5)
# num = int(input("ENTER YOUR NUMBER: "))
# if num == res:
#     print("Число угадано")
# elif num > 5 and num <=0:
#     print("вы были близко")
# else:
#     print("число не угадано")


# ТЕНАРНЫЕ ОПЕРАТОРЫ такой же оператор только в одну строку
# УСЛОВИЕ В ОДНУ СТРОКУ
# ТЕЛО1 if условие else тело2

# a = 5
# res = 'Hello' if a == 4 else 'Bye'
# print(res)

# МАРЖОВЫЙ ОПЕРАТОР ПОЗВ. НАМ ПРИСВАИВАТЬ ЗНАЧЕНИЕ ПЕРЕМЕННОЙ, ТАК И ВОЗВРАЩАТЬ ЕЕ ЗНАЧЕНИЕ

# print(num = 15) - ВЫЙДЕТ ОШИБКА

# print(num :=15)
# print(num)
# print(num + 12)

# import random
# res = random.randomint(0,1)
# num = int(input("enter your number: "))
# if num == 1:
#     print("Congratulation")
# elif num ==

# operator = int(input("enter operator + - / *: "))
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)

# user = int(input("enter your number"))
# if (user%5) == 0 and (user%3) == 0:
#     print('Fizzbuzz')
# elif (user%3) == 0:
#     print("Fizz")
# elif(user%5) == 0:
#     print("Buzz")
# elif (user%5) and (user%3):
#     print("nUMBER")

# res = 'Hello' if a == 4 else 'Bye'
# name = input("Введите ваше имя: ")
# quantity = int(input("колво жрузей: "))
# friends = "друзей" if quantity >= 2 else "ДРУГ"
# result = f'У {name} {quantity} {friends}'
# print(result)

# name1 = int(input("1 side: "))
# name2 = int(input("2 side: "))
# name3 = int(input("3 side: "))
# if name1 == name2 == name3:
#     print("равностронний")
# elif name1 == name2 != name3:
#     print("равнобедренный")
# elif name1 != name2 != name3:
#     print("разносторонний")

# user = input("Создайте пароль: ")
# if user.istitle().lower().int() >=8:
#     print('password is creates')
# else:
#     print("password is not correct")

# user = int(input("Введите пароль из 8 чисел: "))
# if len(user) >=8:
#     print("ваш пароль сохранен")
# else:
#     print("введите корректный пароль")

# math = int(input("Введите свои данные по математике: "))
# english = int(input("Введите свои данные по английскому: "))
# literature = int(input("Введите свои данные по литературе: "))
# user = (math + english + literature)/3
# if user > 69:
#   print("Вы допущены к экзаменам. Ваш средний балл составляет", user)
# else:
#   print("Вы не допущены к экзаменам. Ваш средний балл составляет", user)

x = "name"
print(x[-1:-4])