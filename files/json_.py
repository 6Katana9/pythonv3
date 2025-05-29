'===============JSON=============='
# JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных почти для всех языков программирования

import json 

# json_list = "null"
# print(type(json_list)) # str

# python_list = json.loads(json_list)
# print(python_list) # 

# десериализация - перевод с json строки в python обьект
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

# with open('db.json') as file:
#     list_ = json.load(file)
    # print(list_)

# сериализация - перевод python обьекта в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл 

# json_array = json.dumps(python_list)
# print(json_array)


python_list = [1,2,3, True, False, None] 
with open('db.json', 'w') as file:
    json.dump(python_list, file)


