import string


def int_func():
    line = input("Введите слово: ")
    line2 = string.capwords(line)
    return line2


line_inp = int_func()
print(line_inp)
