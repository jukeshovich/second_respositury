# def post_courses():
#     courses1 = input('Выберите категорию разработки: ')
#     if courses1 == 'Веб-разработка':
#         input('Выберите язык программирования: ')


# print(post_courses())

# def price():
#     sum = int(input('Введите сумму: '))
#     print('Введите валюту: \n\t\tSOM\n\t\tEUR\n\t\tDOL')
#     currency = input('Введите одну из валют: ').lower()
#     if currency == 'SOM':
#         print(sum)
#     elif currency == 'EUR':
#         return sum * 95
#     elif currency == 'DOL':
#         return sum * 87
    
# print(price())

data = [
{
    'id': 1,
    'category': 'Веб-разработка',
    'subcategory': ['Python', 'Java', 'JavaScript'],
    'title': 'Эти уроки будут полезны Веб - разработчикам',
    'description': '10 уроков',
    'level': ['начальный','средний','профессиональный'],
    'price': [100, 150, 200]
},
{
    'id': 2,
    'category': 'Разработка мобильных приложений',
    'subcategory': ['Python', 'Java', 'JavaScript'],
    'title': 'Эти уроки будут полезны мобильным разработчикам',
    'description': '10 уроков',
    'level': ['начальный','средний','профессиональный'],
    'price': [100, 150, 200]
},
{
    'id': 3,
    'category': 'Разработка игр',
    'subcategory': ['Python', 'Java', 'JavaScript'],
    'title': 'Эти уроки будут полезны разработчикам игр',
    'description': '10 уроков',
    'level': ['начальный','средний','профессиональный'],
    'price': [100, 150, 200]
}
]

def getAll():                                               #reading product
    return data

# print(getAll())

def post_product():                                         #creating new product
    max_id = max([i['id'] for i in data])
    new_data = {
        'id': max_id + 1,
        'category': input('Выберите категорию: '),
        'subcategory': input('Выберите язык программирования: '),
        'title': input('Напишите заголовок курса(максимум 60 символов): '),
        'description': input('Напишите описание курса(максимум 10 символов: '),
        'level': input('Выберите уровень: '),
        'price': int(input('Введите сумму: '))
    }
    data.append(new_data)
    return '201 CREATED', new_data
# print(post_product())

def patch_product(id):                                            # changing some product
    product = [i for i in data if i ['id'] == id]
    if product:
        data.extend(product[0])
        category = input('Выберите категорию: ')
        subcategory = input('Выберите язык программирования: ')
        title = input('Напишите заголовок курса(максимум 60 символов): ')
        description = input('Напишите описание курса(максимум 10 символов: ')
        level = input('Выберите уровень: ')
        price = int(input('Введите сумму: '))
        product[0]['Выберите категорию'] = category
        product[0]['Выберите язык программирования'] = subcategory
        product[0]['Напишите заголовок курса(максимум 60 символов)'] = title
        product[0]['Напишите описание курса(максимум 10 символов)'] = description
        product[0]['Выберите уровень'] = level
        product[0]['Введите сумму'] = price
        data.append(product[0])
        return 'Ваше изменение успешно обновлено'
    else:
        return '404', 'Вы ввели неправильный номер'
# print(patch_product(2))

def delete_product(id):                                             # delete some product
    product  = [i for i in data if i ['id'] == id]
    if product:
        data.remove(product[0])
        return 'Продукт успешно удален'
    else:
        return 'Нет такого продукта'
# print(delete_product(2))

def main():
    print('Выберите ваше действие: \n\t\t\t\tПОСМОТРЕТЬ\n\t\t\t\tСОЗДАТЬ\n\t\t\t\tОБНОВИТЬ\n\t\t\t\tУДАЛИТЬ\n\t\t\t\t')
    method = input('Введите один из параметров: ').upper()
    
    if method =='СОЗДАТЬ':
        print(post_product())
    
    elif method == 'ПОСМОТРЕТЬ':
        print(getAll())


    elif method == 'ОБНОВИТЬ':
        id == int(input('Введите ID: '))
        print(patch_product(id))
    
    elif method == 'УДАЛИТЬ':
        id == int(input('Введите ID: '))
        print(delete_product(id))

main()