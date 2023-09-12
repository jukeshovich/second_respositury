# x = int(input())
# y = int(input())
# if x % y == 0:
#     d = x // y
#     print('x делится на y')
#     print(f'Частное: {d}')
# elif x % y != 0:
#     a = x // y
#     b = x % y
#     print('x не делится на y')
#     print(f'Частное: {a}')
#     print(f'Остаток: {b}')


# year = int(input())
# if year % 4 == 0 and year % 100 !=0:
#     print('YES')
# elif year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# count = 0
# number = input()
# if number.isdigit():
#     count += number
# print(count)

# courses = 600
# sale = int(input('vvedite skidku: '))
# res = courses / 100 * sale
# res2 = courses - res
# print(res2)
# res3 = res2 / 4
# print(res3)

# def func(name):
#     name1 = list(name)
#     print(name1)
#     return name1

# def func2(name2):
#     vowels = ['a','e','y','u','i','o']
#     work = [i for i in name2 if i in vowels]
#     res = ''.join(work)
#     return res

# a = input()
# print(func2(func(a)))

# num = 6

# def check(num):
#     if num % 2 != 0:
#         return('it is odd number')
#     if num % 2 == 0:
#         return('it is even number')
# print(check(num))

# num = 6

# def check(num):
#     if num % 2 == 0:
#         return('it is even number')
#     else:
#         return('it is odd number')

# print(check(num))

# list_ = [i for i in range(1,101)]
# print(list_)

list_ = [i for i in range(2,51,2)]
print(list_)