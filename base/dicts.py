# # # # # '=================Словари=============='
# # # # # # dict - изменяемый, итерируемый, неупорядоченный(псевдопорядок), неиндексируемый тип данных, для хранения данных в парах (ключ:значение)

# # # # # user = {
# # # # #     'name':'Katana',
# # # # #     'cars':['bmw', 'mers'], 
# # # # #     'age':21, 
# # # # #     'prof':'Dev'
# # # # #     }

# # # # # print(user['cars']) # Katana

# # # # # # ключами в словаре могут быть только не изменяемые типы данных
# # # # # # значениями могут быть любые типы данных

# # # # # dict1 = {'c':1, 'a':10, 'b':2, 'a':'hi'}
# # # # # print(dict1['a']) # если ключи одинаковые, сохранится только последнее значение
# # # # # print(dict1)

# # # # # '================Создание=============='
# # # # # dict1 = {'a':1, 'b':2}
# # # # # dict2 = dict([ [1,2], [2,3], [3,4] ])
# # # # # print(dict2) # {'a':1, 'b':2, 'c':3}

# dict4 = {'name':'Sultan'}
# dict4['name'] = 'katana'
# dict4['age'] = 21

# # # # print(dict4)

# # # # '===============Методы словаря==========='
# # # # # get - метод, который возвращает значение по ключу, если такого ключа нет, то выйдет None или дефолтное значение

# # # # user = {'name':'Metalabs', 'age':4, 'course':'python'}

# # # # print(user['title']) # KeyError
# # # # print(user.get('title')) # None


# # # # # pop - удаляет пару по ключу и возвращает значение

# # # # user = {'name':'Metalabs', 'age':4, 'course':'python'}
# # # # popped_value = user.pop('name')

# # # # # popitem - даляет последнюю пару и возвращает ее 
# # # # user = {'name':'Metalabs', 'age':4, 'course':'python'}
# # # # popped_item = user.popitem() 
# # # # # ('course', 'python')


# # # # # update - расширяет словарь парами из второго словаря
# # # # dict1 = {1:'a', 2:'b'}
# # # # dict2 = {2:'c', 4:'d'}
# # # # dict1.update(dict2)

# # # # print(dict1) # {1:'a', 2:'c', 4:'d'}
# # # # print(dict2) # {2:'c', 4:'d'}

# # # # # clear - очищает словарь
# # # # dict1 = {1:'a'}
# # # # dict1.clear() # {}

# # # # fromkeys - метод для создани нового словаря, используя список ключей
# # # dict1 = dict.fromkeys('hi', True)
# # # print(dict1)

# # # # keys, values, items
# # # # keys - метод, который возвращает ключи
# # # # values - метод, который возвращает значения
# # # # items - метод, который возращает пары

# # # user = {
# # #     'name':'Sultan',
# # #     'age':22,
# # #     'prof':'Dev'
# # # }
# # # print(user.keys())
# # # print(user.values())
# # # print(user.items())

# # # '==============Итерирование словарей======='
# # # for i in user:
# # #     print(i)

# # # for key in user.keys():
# # #     print(key)

# # # for value in user.values():
# # #     print(value)

# # user = {
# #     'name':'Sultan',
# #     'age':22,
# #     'prof':'Dev'
# # }

# # for k, v in user.items():
# #     print(k, 'hi', v)

# # # k, v = ('name', 'Sultan')
# # # k, v = ('age', 22)
# # # k, v = ('prof', 'Dev')

# # # a, b, c = 20, 4, 2

# # # вам н словарь
# # # создайте новый словарь, поменяв ключи со значениями
# # # {1:'a', 2:'b'}


# dict1 = {'a':1, 'b':2}
# dict2 = {}
# for k, v in dict1.items():
#     dict2[v] = k
# print(dict2)


# '===================Set==============='
# # set(множество) - изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных, предназначенный для хранения уникальных значений. Множество может хранить в себе только неизменяемый типы данных

# list1 = [12, 2,3, 12, 2, 2,2,2,2,2,2,45,23,1,1,1,0,0]

# set1 = {1,2,3,'hi',4, 5, 5, {2,3,4}}

# # list, dict, set 

# set1 = set(list1)

# list1 = list(set1)
# # print(list1)

print(dir(set))

# add - добавляет элемент в set
set1 = {1,2,3}
set1.add(4)
set1.add(3) 
# {1,2,3,4}

# pop - удаляет случайный элемент из set (но есть принцип FIFO)
set2 = {1,2,3}
popped = set2.pop()
print(popped) 

# remove - удаляет элемент из set по значению
set3 = {1, 2, 'hi', 3}
set3.remove(3)
print(set3) # {1,2,'hi'}

# difference (-) - находит элементы, которые не встречаются в другом set 
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.difference(set2)) # {1,2}
print(set1 - set2) # {1, 2}

print(set2.difference(set1)) # {4,5}
print(set2 - set1) # {4, 5}

# symmetric_difference - находит те элементы которых нет в обоих сетах
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.symmetric_difference(set2)) 
# {1,2,4,5}

# intersection (&) - находит похожие элементы в сетах
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2)) # {3,4}
print(set1 & set2) # {3, 4}

# update - добавляет элементы из другого сета в текущий сет
set1 = {1,2,3}
set2 = {3,4,5}
set1.update(set2) # {1,2,3,4,5} 

print(dir(set1))