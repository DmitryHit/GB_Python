n = int(input('Введите число, нажмите Enter, получите факториал: '))


def fact(n):
    start = 1
    for x in range(1, n+1):

        start = start * x
        yield start


for el in fact(n):
    print(el)
