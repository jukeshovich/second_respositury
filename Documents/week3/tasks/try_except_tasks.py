# try:
#     num1 = input('enter etwas: ')
#     num2 = input('enter etwas: ')
#     result = int(num1) + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)

# dict1 = {1: 'erlan', 2: 'Allan', 3: 'Bob'}
# dict1 = {value: key for key, value in dict1.items()}
# print(dict1)
# try:
#     username = input('enter username: ')
#     id1 = dict1[username]
#     print(id1)
# except KeyError:
#     print('Введенного username нет в базе данных')
# else:
#     print(f'Добро пожаловать {username}')
# finally:
#     print('спасибо')

# try:
#     age = int(input('ENTER YOUR AGE: '))
#     if age <=0:
#         raise Exception('Ваш возраст должен быть больше 0')
# except ValueError:
#     print('Введите число, не строку')
# else:
#     print(f'Ваш возраст: {age}')


