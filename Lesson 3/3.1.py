def my_func(num1, num2):
    try:
        res = num1 / num2
        return res
    except ZeroDivisionError:
        return 'На ноль нини'


print(my_func(int(input('Введи первое число: ')), int(input('Введи второе число: '))))
