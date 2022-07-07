def my_sum():
    sum_now = 0
    symbol = False
    while not symbol:
        num = input('Введите число или Q для выхода: - ').split()
        result = 0
        for el in range(len(num)):
            if num[el] in ['Q']:
                symbol = True
                break
            else:
                try:
                    result = result + int(num[el])
                except ValueError:
                    print('Вводи только числа или спец символ')

        sum_now = sum_now + result
        print(f'Сумма равна: {sum_now}')


my_sum()
