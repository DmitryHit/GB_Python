data_list = [3, 2, 1, 11, 2, 33, 12, 13, 2, 14, 7, 1, 2]
data = [el for el in data_list if data_list.count(el) == 1]
print(data)
