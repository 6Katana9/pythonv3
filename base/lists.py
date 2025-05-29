# # # '==================Списки=============='
# # # # list - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для храения любых типов данных в определенном порядке

# # # # list1 = [12, [1, [0,0,5], 2,3], 'hello', -4, 1, 'katana', True, False, 20.9, None]

# # # # print(list1[1][1][-1])

# # # #range(start, end, step) - функция, которая создает последовательность от start до end, если есть step то сделает с шагом

# # # a = list(range(50))
# # # print(a)

# # '================Методы списков==========='
# # # append - добавляет элемент в конец списка
# # list2 = []
# # list2.append(1)
# # print(list2)
# # list2.append('hello')
# # print(list2)
# # list2.append([1,2,3])
# # print(list2)

# # # [1, 'hello', [1,2,3]]


# # # pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если индекс не указать то удалит последний элемент

# # # list3 = []
# # # popped_elem = list3.pop()


# # # remove - удаляет элемент из списка по значению
# # list2 = [1,2,3,'hello',5,1,1,1]
# # list2.remove()

# # count - считает кол-во принятого элемента в списке
# # list2 = ['hello', True, False, 'hi', 98, 1, 1, 1]
# # print(list2.count(0))

# # list2 = ['hi', 'hello', 'metalabs', 'katana', 'nick', 'hello world', 1, 23, True]
# # print(list2.index(True))

# # insert - добавляет элемент в список по индексу 
# # list2 = ['hi', 'hello', 'metalabs']
# # list2.insert(1, 'world')

# # print(list2)

# # extend - добавляет элементы принятного списка в первый список, изменяя его

# list1 = [1,2,3]
# list2 = [0,0,0]
# # list1.append(list2) # [1,2,3,[0,0,0]]
# list1.extend(list2) # [1,2,3,0,0,0]

# # reverse - изменяет список, расставляя его элементы в обратном порядке
# # list1 = [1,'hi',3, 'hello', 5, [1,2,3]]
# # #[[1,2,3], 5, ...]
# # list1.reverse()
# # print(list1)

# # sort - сортирует список, состоящий из элементов одного типа данных
# # list2 = [23, 4, 25, 0, -1, 6]
# # list2.sort()
# # print(list2)

# # list3 = ['A', '+', 'a', 'B', 'Hi', 'Hello', '23']
# # list3.sort(key=len)
# # print(list3)

# # clear()

# # print(dir(list))

# # a = 5
# # b = 6
# # c = 4

# # a, b, c, d = 5, 6, 4  


# # tuple - не изменяемый тип данных, литералы - (,) 
# # 2 метода - index, count


# a = 'hi'
# b = 'hi'
# print(a is b)

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)

# a = (1,2,3)
# b = (1,2,3)
# a is b 

# # b = (1,2,3) + (1,2,3)

# # print(b)

# # for elem in [23, 4, 5]:
# #     print('hello')

# # meshok = ['kartosha', 'pomidor', 'luk', 'kartoshka']

# # for ruka in meshok:
# #     if ruka == 'luk':
# #         print('не люблю лук')
# #     else:
# #         print(f'В руке - {ruka}')


# # у вас есть list1 = [23, 1, 2, 4, 56, -29]
# # вы должны отсортировать этот лист на list2 и на list3. В лист2 будут четные числа, а в лист3 нечетные

# list1 = [23, 1, 2, 4, 56, -29]
# list2 = []
# list3 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)
#     else:
#         list3.append(i)
# print(list2)
# print(list3)


# a = [12, 'hi', 2, True]
# list_ = []
# list2 = []
# list3 = []
# for i in a:
#     if type(i) == str:
#         list_.append(i)
#     elif type(i) == int:
#         list2.append(i) 
#     else:
#         list3.append(i)
# print(type(True)==bool)


