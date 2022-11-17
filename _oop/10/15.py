# def extendList(item, list=[]):
#     list.append(item)
#     return list
#
# list1 = extendList(11)
# list2 = extendList(156,[])
# list3 = extendList('c')
#
# print("list1 = {}".format(list1))
# print("list2 = {}".format(list2))
# print("list3 = {}".format(list3))

# import math
#
# print(math.floor(5.5))
#
# result = (80 - 12*5) / 4
# print(result)
#
# x = 4.5
# y = 2
# print(x//y)

# nums = set([1,1,2,3,3,3,4])
# print(len(nums))

# name='SoftServe' #"SoftServe IT  Academy"
# # name.replace("o", "Q")
# name.title()
# print(name)
#
# names=['ram', 'raj']
# print("\n".join(names))

#
# one = chr(104)
# two= chr(105)
# print(one + two)
#
# my_tuple = (1,2,3,4)
# my_tuple.append((5,6,7))
# print(len(my_tuple))

# print(type(1J))
#
# def f(): pass
# print(type(f()))

# foo = {}
# print(type(foo))
#
# def divisible_by_five(number):
#     if number % 5 == 0:
#         return True
#     else:
#         return False
#
#
# print(divisible_by_five(5))
#
# def find_odd(lst):
#     lst2 = []
#     for i in lst:
#         b = lst.count(i)
#         if b % 2 != 0:
#             if i not in lst2:
#                 lst2.append(i)
#     return lst2
# print(find_odd([1, 1, 1, 5, 5, 5]))
#
# def card_hide(card):
#     if len(str(card)) < 16:
#         return "Invalid card"
#     else:
#         return ('*'*12) + str(card)[12:16]
#
# print(card_hide(12345456788965866))
#
# while (3==3):
#     print('1')
# list_value = [None, 3, None, 5, None, None, 14]
# res = [i for i in range(len(list_value)) if list_value[i] == None]
# print(f"The original list : {list_value}")
# print(f"The None indexes list is : {res}")

# def parse_number(num):
#     try:
#         num_to_str = str(num)
#         count_of_odd = [int(x) for x in num_to_str if not int(x) % 2 == 0]
#         count_of_even = (int(x) for x in num_to_str if int(x)%2 == 0)
#         return {'odd':count_of_odd, 'even':count_of_even}
#     except ValueError:
#          return False
#      except TypeError:
#         return False