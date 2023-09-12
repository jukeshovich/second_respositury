# numbers_str = input("Введите цифры через запятую: ").split(',')
# numbers_int =[]
# for number in numbers_str:
#     numbers_int.append(int(number))
# print(numbers_int[0], numbers_int[-1])

# numbers_int.pop()
# numbers_int.append("Makers")
# print(numbers_int)

# from random import sample

# numbers = sample(range(0, 10), k = 10)
# print(numbers)
# print(sorted(numbers))


list_lenght = int(input("Enter list lenght: "))
words = []
words_lenght = []
for i in range(list_lenght):
    word = input("Enter word: ")
    words.append(word)

for i in words:
    words_lenght.append(len(i))

print(words)
print(words_lenght)


