def wage():
    production_in_hours = (float(input('Укажите количество отработаных часов: ')))
    hourly_rate = (float(input('Укажите ставку оплаты в час: ')))
    premium = (float(input('Укажите размер премии для сотрудника: ')))
    pay = production_in_hours * hourly_rate
    return pay + premium


print(f'Заработная плата равна: {wage()} у.е.')
