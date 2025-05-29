# '================Циклы=============='
# # цикл - это блок кода, который отрабатывается несколько раз
# # for - цикл, который работает с итерируемыми обьектами. Цикл for заканчивает свою работу, когда он доходит до последнего элемента итерируемого обьекта
# # while - цикл, который работает до тех пор пока условие верное

# # итерируемый обьект - последовательность по которой мы можем пройтись (list, str, tuple)
# # итерация - один круг в цикле (процесс работы цикла)

# list_ = [12, 3, 4, 'hi', 4]
# str_ = 'hello'

# for elem in list_:
#     print(elem)


# 'FOR'
# list_1 = [23, 2, 4, 12, 'hi', 2, 3, 4,5]

# # list(range(1, 13, 2))
# # [1,3,5,7,9,11]

# # str_1 = 'hello world'
# a = range(1, 10000, 2)
# for i in a:
#     print(i)


'WHIL'
# n = 10
# while n > 0:
#     n -= 1 # n = n + 1
#     print(n) 

# a = True
# while a:
#     print(1)

# list_ = [1,2,3,4,5]
# n = 0
# while 2+n in list_:
#     print('hi')
#     n += 1
#     list_[1] + 2


'============Ключевые слова в циклах========'
# break - полностью останавливает работу цикла
# continue - переходит к следующей итерации

# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(11):  
#     # 0,1,2,3,4,5,6,7,8,9, 10
#     print(i)
#     break



# for i in range(11):
    # if i == 3:
    #     break
    # print(i)


# count = 0
# while count <= 10:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count += 1


# count = 0
# while count < 100:
#     print(count)
#     count += 1
#     if count == 3:
#         break

for i in range(11):
    print(i)
else:
    print('Цикл фор завершил работу естественно')

count = 0
while count < 10:
    # break
    print(count)
    count += 1
else:
    print('Цикл while завершил работу естественно')