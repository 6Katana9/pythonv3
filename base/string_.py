# # '===============Строки=============='
# # # строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

# # string1 = 'hello world'
# # string2 = "hello world"

# # string3 = "Don't"
# # string4 = 'my name is "Sultan"'

# # string5 = 'hello' + ' ' + 'world' # конкатенеция

# # string7 = 'hello world ' * 100
# # # print(string7)

# # '=================Экранизация==============='
# # '\n' # перенос строки на новую
# # # print('hello\nworld\nkatana')
# # # print('hello world katana')

# # '\t' # табуляция
# # # print('hello\tworld')


# # '\\' # отображение \

# # string9 = 'Don\'t'
# # print(string9)

# # string10 = '\\t - это табуляция'
# # print(string10)

# # '\v' # перенос на новую строку со смещением вправо на длинну предыдущей строки

# # string11 = 'hello\vworld\vmetalabs'
# # print(string11) 

# # '\r' # перенос каретки на начало строки 
# # string12 = '  Hello world\rBB123'
# # print(string12)
# # # 
# '==================Форматирование строк==============='
# title = 'iPhone16pro'
# price = 153000

# #1
# info = f'Название товара: {title}\nЦена: {price}'
# print(info)

# #2
# info = 'Название товара: {}\nЦена: {}'
# print(info.format(title, price))
# print(info.format('Mi', 70000))

# #3
# info = 'Название товара: %s\nЦена: %s'
# print(info % (title, price))
# print(info % ('SamsungZflip', 150000))

'=====================Методы строк================='
# методы - функции, которые относятся к определенному типу данных, к ним мы обращаемся через точку

print(dir('dgdfd'))

'HELlo'.lower() # hello
'heLLo'.upper() # HELLO 
'HeLLO WoRld'.swapcase() # hEllo wOrLD

'heLLO woRlD'.title() # Hello World
'heLLO woRlD'.capitalize() # Hello world

print('helLo world'.count('l')) # 2

print(dir(int))
