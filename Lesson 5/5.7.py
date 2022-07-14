import json
profit = {}
positive_profit = 0
average_profit = 0
i = 0
with open('5.7.txt', encoding='utf-8') as file:
    for el in file:
        name, type_of_ownership, earning, costs = el.split()
        profit[name] = int(earning) - int(costs)
        if profit.setdefault(name) >= 0:
            positive_profit = positive_profit + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = positive_profit / i
        print(f'Средняя прибыль: {average_profit:.2f}')

    print(f'Прибыль каждой компании: {profit}')

with open('5.7.json', 'w') as write_js:
    json.dump(profit, write_js)

with open('5.7.json', encoding='utf-8') as f:
    js_str = json.load(f)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
