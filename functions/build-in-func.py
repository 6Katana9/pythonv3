# # # '===========Встроенные функции=========='
# # # # map, filter, reduce, zip, enumerate


# # # # zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# # # list1 = [1,2,3,4,5]
# # # list2 = ['a', 'b', 'c']
# # # list3 = [10.5, 3.0, 5.5, 4.1]

# # # zipped = zip(list1, list2)
# # # # print(zipped)
# # # # print(list(zipped))
# # # # for i in zipped:
# # # #     print(i)

# # # print(dict(zipped))


# # # enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)

# # enumerated = enumerate(['hi', 'hello', 'metalabs'])
# # print(list(enumerated))


# # # map - функция высшего порядка, которая принимает первым аргументом другую функцию и вторым аргументом последовательность, получаем генератор

# # list_1 = ['1', '2', '3', '4']
# # mapped = map(int, list_1)
# # print(list(mapped)) # [1, 2, 3, 4]


# # list2 = [23, 1, 45, 6]
# # def func(x):
# #     return x ** 2

# # mapped = map(func, list2)
# # print(mapped)


# list2 = [23, 1, 45, 6]
# mapped = map(lambda x: x ** 2, list2)
# for i in mapped:
#     print(i)


# # filter - функция высшего порядка, которая принимает первым в аргументы другую функцию, а вторым аргументом принимает последовательность. Работает с теми функциями, которые возвращают булевое значение (True, False). Получаем генератор
# # (фильтр возвращает генератор, с элеменатами, прошедшим фильтр (какоето условие))


# list_4 = [3, 0, -10, 34, -5]
# filtered = filter(lambda x: x > 0, list_4)
# print(list(filtered))


# # reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)

# from functools import reduce 

# list5 = [1,2,3,1,5,22,166]
# res = reduce(lambda x, y: x + y, list5)
# print(res)


# # напишите декоратор который будет выводить слово hello в терминале, перед запуском функции

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('hello')
#         func()
#     return wrapper

# @decorator
# def func():
#     print('hi')

# func()

# # + 
# # -
# # /  //
# # *
# # **
# # % 
# # x ** 0.5

# # from math import sqrt 

# # sqrt(81)

# # "asdfghjk"
# # [12, 2, 5]
# # {:}
# # {}
# # (,)

# # print(dir(str))
# # print('heLLo world'.capitalize())
# # print('hello woRld'.title())

# # var = [1,2,3,4]
# # var.append(5)
# # print(var)


# # var = 'hello|world|metalabs'
# # var2 = var.split('|') 
# # print(var2)

# # x = 12

# # if x > 0:
# #     num = 23
# # else:
# #     num = 14

# # num = 23 if x > 0 else 14



list1 = [[1,2,3], [11, 22, 33], [111, 222, 333]]
list2 = []
for i in list1:
    for j in i: 
        list2.append(j)
print(list2)

