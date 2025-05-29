# # '=============Области видимости==========='
# # # LEGB - local enclosed global build-in

# # '================Build-in================='
# # # встроенное пространство имен (print, list, int, input)

# # # print()

# # '==================Global================='
# # # все переменные, которые мы создаем внутри файла
# # a = 5 
# # b = 'hello'
# # print(globals())
# # def func():
# #     ...

# # '===============Local================'
# # # локальное пространство имен - переменные,  созданные внутри функции

# a = 10

# def func(a, b):
#     print('Глобальное', globals())
#     print('Локальное', locals())
#     print(a, b)
    
# func(12, 4)

# '================Enclosed=============='
# # замкнутое пространство имен - локальное пространство, у которого есть внутри локальное пространство

# var = 'global' 

# def func():
#     # локальное пространство для глобального пространства
#     # замкнутое постранство (потомучто есть более локальное пространство)
#     var = 'enclosed'
#     def inner_func():
#         # локальное пространство 
#         var = 'local'


# # chelovek1 = 1
# # chelovek2 = 2

# # def mashina():
# #     chelovek3 = 3
# #     print(chelovek1)
# #     print(chelovek2)

# # print(chelovek3)
# # func()

# # локальное пространство видит глобальное пространство
# # глобальное пространство не видит локальное


# count = 1 

# def increase_count():
#     global count 
#     a = 10
#     print(count)
#     count += 1

# increase_count()
# increase_count()
# increase_count()
b = 20

def func1(i):
    a = 0 
    global b
    b = 11

    def func2():
        nonlocal a
        a = 20

        def func3():
            nonlocal a
            a = 20
            return 'hello'

        
      

# локальное пространство видит глобальное пространство
# глобальное пространство не видит локальное
# оператор global - дает доступ на изменение переменной из глобального пространства
# оператор nonlocal - дает доступ на изменение переменной из замкнутого пространства



# калькулятор на функции. calc(num1, num2, oper), return res

# print(calc(10, 5, '-'))

def calc(num1, num2, oper):
    if oper == '+':
        res = num1 + num2 
    elif oper == '-':
        res = num1 - num2 
    elif oper == '/':
        res = num1 / num2 
    elif oper == '*':
        res = num1 * num2 
    elif oper == '**':
        res = num1 ** num2 
    elif oper == '%':
        res = num1 % num2 
    return res 

print(calc(10, 5, '/'))
print(calc(200, 100, '*'))