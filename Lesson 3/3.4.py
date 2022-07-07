# def my_func(number, negative):
#
#     if negative == 0:
#         return 1.0
#
#     if negative < 0:
#         negative *= -1
#
#     return 1.0 / (number ** negative)
#
#
# print(my_func(number=int(input("Введите число:")),
#               negative=int(input("Введите степень:"))))


def my_func(number, negative):

    if negative == 0:
        return 1.0
    if negative < 0:
        negative *= -1

    power = number
    for i in range(1, negative):
        number *= power

    return 1.0 / number


print(my_func(int(input("Введите число:")),
              int(input("Введите степень:"))))
