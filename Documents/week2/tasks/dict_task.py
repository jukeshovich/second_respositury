# university = {
#     'программирование': 150,
#     'экономика': 98,
#     'медицина': 82
# }
# # 1
# # university['экономика'] = 120
# # print(university)
# # 2
# # university['лингвистика'] = 56
# # print(university)
# # 3
# # university.update({'лингвистика': 56})
# # print(university)

# university.setdefault('лингвистика', 60)
# print(university)

# print(university.pop('медицина'))
# # print(university)
# print (sum(list(university.values())))


# 2
# dict1 = {1: "a", 2: "b", 3: "c"}
# new_dict = {}
# for key, val in dict1.items():
#     new_dict.update({val: key})
# print(new_dict)



# count = int(input("How many do you want to invite: "))
# quest = {}
# for i in range(1, count +1):
#     name = input("Enter quest name: ")
#     quest.setdefault(i, name)

# print(quest) 


# my_list = [
# {'potato': 4},
# {'milk': 2},
# {'bread': 3},
# {'eggs': 20}
# ]
# while my_list:
#     product_remove  = input()
#     for products in my_list:
#         if product_remove in products:
#             del products[product_remove]
#             print(my_list)

#     if not any(my_list):
#         break
# print('Time to pay')
# print('stop')