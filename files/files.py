'===========Модули и пакеты=========='
# любой файл с расширением .py - модуль
# пакет - набор модулей (обязательно должен быть файл __init__.py)

'=============Работа с файлами==========='
# open - функция, которая открывает файл в определенном режиме

'Режимы:'
# r - read(только для чтения)
# w - write(только для записи, каждый раз файл очищается)
# a - append(только для дозаписи, добавляет в конец)
# x - создает файл, но если он существует выйдет ошибка

'==================Read=============='
# file = open('test.txt', 'r')
# print(file.writable()) # False (проверяет можно ли записать в этот файл чтолибо)
# print(file.readable()) # True (можем читать, так как открыли в режиме чтения)
# text = file.read(7) 
# file.seek(0)
# print(file.read())

# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())


# print(file.readlines()) # получаем все строки ввиде листа
# file.seek(0)
# print(file.readlines())
# file.closed() # False
# file.close()
# file.closed() # True

# '================Write==============='
# file = open('new_file.txt', 'w')
# # если файл не существует - создаст его

# print(file.readable()) # False
# print(file.writable()) # True

# # file.write('Hello\nworld\n')
# # file.write('Metalabs')

# # file.writelines(('AAAA\n',))

# file.close()

# '===============Append==========='
# file = open('new_file.txt', 'a')
# file.write('BBBB\n')
# file.close()



# '=============Контекстный менеджер========='
# # конструкция with 

# with open('test.txt') as f:
#     print(f.closed) # False
#     print(f.read())
#     print(f.closed) # False
# print(f.closed) # True




# list2 = [-12, 4, 0, -3, 12]
# Использя filter вам нужно оставить только отрицательные числа 
# list3 = [-12, -13]

# filter, lambda(def)

list2 = [-12, 4, 0, -3, 12]
filtered = filter(lambda x: x < 0, list2)
print(list(filtered))