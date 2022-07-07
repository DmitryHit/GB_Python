from functools import reduce as re

data_list = [el for el in range(100, 1001, 2)]
sum_num = re((lambda a, b: a * b), data_list)

print(sum_num)
