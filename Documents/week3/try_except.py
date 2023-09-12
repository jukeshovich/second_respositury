# есть исключения и ошибки это обьекты которые прерывают работу кода
# ошибки - проблема в синтаксисе (которые мы исправляем самостоятельно)

# 1. SyntaxError: забыли двоеточие, неправиотно назвали переменную забыли ковычки или скобки.

# 2. IndentationError: ошибка табуляции или неправильный отступ 

# 3. TabError: неверная табуляция(смешивание пробелов и табов)


# ИСКЛЮЧЕНИЯ - КОД НАПИСАН ВЕРНО НО НАША ПРОГРАММА РАБОТАЕТ НЕ ТАК КАК ОЖИДАЛАСЬ

# ZeroDivisionError выходит при делении на ноль 45/0. 45//0. 45%0

# NameError когда нет переменной на которую мы ссылаемся выходит эта ошибка

# IndexError исключение которая выходит когда обращаемся к несуществующему индексу

# KeyError исключения которое выходит когда мы обращаемся к несуществующему ключу

# метод get() не вызывает ошибку

# ImportError исключения которые не существуют в файле которые мы импортируем 

# ValueError когда в функцию передаем не тот тип данных а также выходит когда мы делаем конкатенацию числа и строки

# TypeError выходит когда мы пытаемся использовать методы не свойственные какому то типу данных
# либо же когда мы передаем в функцию больше или меньше аргкментов чем ожидает функция

# for i in 123:     TypeError
#     print(i)

# [1,2,3].append()  TypeError: append() takes exactly one argument (0 given)

# AttributeError - выходит когда мы обращаемся к несуществующему методу обьекта или аттрибуту

# [].replace('a','') - AttributeError: 'list' object has no attribute 'replace' так как эта функция не раюотает со списком

# BaseException() - отец всех ошибок которые выше и не только 

# tryexcept 
# МЫ ИСПОЛЬЗУЕМ ЭТО СТРОЕНИЕ ДЛЯ ТОГО, ЧТОБЫ НАШ КОД НЕ ПРЕКРАЩАЛ РАБОТУ
# СТРУКТУРА

# try:
#     код который может вызвать ошибку 
# except:
#     который сработает если в try вышла ошибка
# else:
#     код который сработает если в try не вышла ошибка
# finally:
#     код сработает в любом случае

# try:
#     age = int(input('enter your age: '))
# except:
#     print('hello world')

# try:
#     age = int(input('enter your age: '))
# except ValueError:
#     age = int(input('enter your age again: '))

# try:
#     a = 5
#     b = 0
#     res = a/b
# except ZeroDivisionError:
#     print('error')


# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')

# try:
#     int('f')
# except ValueError:
#     print('Неверный код')
#     try:
#         3/0
#     except ZeroDivisionError:
#         print('деление на ноль')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1/num2
#     print(res)
# except (ZeroDivisionError, ValueError):
#     print('Произошла ошибка!')

# try:
#     dict_ = {key: key**2 for key in range(1000) if key %a == 0}
# except NameError:
#     print('ПЕРЕМЕННОЙ A НЕТ')
#     try:
#         a = int(input('укажите число: '))
#         dict = {key: key**2 for key in range(1000) if key %a == 0}
#         print(dict_)
#     except ValueError:
#         print('a должен быть число')
#         a = int(input('укажите число'))
#         dict_ = {key: key**2 for key in range(1000) if key %a == 0}
#         print(dict_)

# try:
#     num1 = int(input('enter num: '))
#     num2 = int(input('enter num: '))
#     result = num1/num2
#     print(result)
# except ValueError:
#     print('вы ввели неправильные данные')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')

# dict1 = {'a':5 , 'b': 10, 'c':15, 'd':20}
# try:
#     key = input('enter key: ')
#     value = dict1[key]
# except KeyError:
#     print('нет такого ключа')
# else:
#     value *= value
#     print(value, 'block else')

# try:
#     result = a * 2
#     print(res)
# except Exception as e:
#     print(f'Возникла ошибка {e.__class__}') #->Возникла ошибка <class 'NameError'>
# finally:
#     a = 5
#     result = a*1
#     print(result, 'block finally')

# raise - искусственно вызывает ошибку

# number = int(input('enter: '))
# if number > 5:
#     raise 'значение не должно быть больше 5'

# age = 20
# if age > 18:
    # raise Exception('error')
    # raise ValueError('f')

# try:
#     if 2 > 1:
#         raise ValueError
# except ValueError:
#     print('возраст больше 2')


# ==========================================================================================================================================================


# try:
#     num1 = int(input('Введите число: '))
# except:
#     print('Вы ввели не число')

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     res = num1/num2
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# except ValueError:
#     print('Вы ввели не число')
# else:
#     print(res)
# finally:
#     print('Программа завершена')

# dict1 = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict1 = {key: len(key) for key, val in dict1.items()}
# dict1.update({'except': 'Exception'})
# print(dict1)

# while True:
#     try:
#         key = input('Введите слово: ')
#         if key == 'exit':
#             break
#         dict1[key] += 2
#     except (KeyError, TypeError):
#         print('Такого ключа нет в словаре или вы не можете провести конкатенацию с числами')
#     else:
#         print(dict1[key])
#     finally:
#         print(dict1)

# list1 = [i for i in range(1,31)]
# try:
#     index = int(input())
#     list1[index] = 'Makers'
# except IndexError:
#     print('Вы вне диапазона')
# except ValueError:
#     print('Введите число не строку')
# else:
#     print('нет ошибок')
# finally:
#     print(list1)

# try:
#     print(makers)
# except NameError:
#     print('переменная не найдена')

# number = int(input('enter number from 1 to 70: '))
# if number not in range(1,71):
#     raise Exception('You entered the number more than 70')
# print('ok')

  
try:
    age = int(input())
    if age < 18:
        raise Exception('Доступ запрещен')
except ValueError:
    print('Введен некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания!')




