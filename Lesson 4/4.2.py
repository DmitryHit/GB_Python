data_list = [5, 100, 900, 354, 7, 28, 19, 600, 5, 400, 4000, 4000000]

data = [data_list[el] for el in range(len(data_list)) if data_list[el] > data_list[el - 1]]

print(data)
