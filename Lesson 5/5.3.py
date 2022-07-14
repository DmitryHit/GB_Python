with open('5.3.txt', encoding='utf-8') as file:
    salary = []
    Less = []
    file_split = file.read().split('\n')
    for el in file_split:
        el = el.split()
        if float(el[1]) < 20000:
           Less.append(el[0])
        salary.append(el[1])
print(f'Оклад меньше 20.000 - {Less}.\nCредний оклад: {sum(map(float, salary)) / len(salary)}')
