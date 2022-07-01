goods = []
categories = (
    'Название',
    'Цена',
    'Количество',
    'Единица измерения',
)

while True:
    print('***ТОВАРЫ***')
    print('1. Добавить товар\n2. Посмотреть товары\n3. Аналитика\n4. Выход')
    print('************')
    select = input('Выберите необходимый пункт меню - ')

    if select == '1':
        item = {}
        for category in categories:
            item[category] = input(f'{category} товара: ')
        goods.append(item)
        print('************\n!Товар был успешно добавлен!\n')

    elif select == '2':
        print('***КАТАЛОГ***\n')
        for item in enumerate(goods, 1):
            print(item)

    elif select == '3':
        analytics = {}
        for good in goods:
            for categories, item in good.items():
                if categories in analytics:
                    analytics[categories].append(item)
                else:
                    analytics[categories] = [item]

        print(analytics)
        break

    elif select == '4':
        break

    else:
        print('ERROR выберите пункт меню!')
