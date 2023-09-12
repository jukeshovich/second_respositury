# okroshka = {'potato', 'eggs', 'cucumber',
#             'wurst', 'grass'}
# olivie = {'potato', 'marine cucumber', 'wurst', 'carrot', 'eggs'}
# common = (len(okroshka.intersection(olivie)))
# print(common)

# unique_okroshka = okroshka.difference(olivie)
# unique_olivie = olivie.difference(okroshka)
# print(unique_okroshka)
# print(unique_olivie)

# users = {
#     ('Alice', 'Python', 5),
#     ('John', 'Python', 6),
#     ('Ann', 'JavaScript',1),
#     ('Alice', 'JavaScript', 2),
#     ('Rachel', 'Python', 8),
#     ('Rachel', 'JavaScript', 9)
# }
# countPython = 0
# countJS = 0
# setPython = set()
# setJS = set()
# for info in users:
#     countPython += info.count('Python')
#     countJS += info.count('JavaScript')

#     if info[1] == 'Python':
#         setPython.add(info[0])
#     else:
#         setJS.add(info[0])
# print(countPython)
# print(countJS)
# print(setPython & setJS)

while True:
    currency = input('Введите валюту (сом или доллар): ')
    sum = int(input(f'Введите сумму которую вы хотите перевести в {currency}ы: '))
    
    if currency == 'доллар':
        result = sum / 84.80
        print(f'{round(result, 1)} $')
    elif currency == 'сом':
        result = sum *84.80
        print(f'{round(result, 1)} сом')
    else:
        print('Введите правильные данные')
        continue
    choise = input('Хотите продолжить?: ')
    if choise.lower() == 'да':
        continue
    else:
        print('Всего хорошего!')
        break





