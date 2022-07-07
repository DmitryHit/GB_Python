def person(name, surname, year, city, email, phone):
    print(f'{name}, {surname}, {year}, {city}, {email}, {phone}')


person(name='Pipa', surname='August', year='1919', city='Taganda', email='saba4ka@net', phone='999-99-99')

# def person():
#     data = {}
#
#     config = ['name', 'surname', 'year', 'city', 'email', 'phone']
#
#     for param in config:
#         data[param] = input(f'Введите значение поля {param} - ')
#
#     return data
#
#
# info = str(person())
# print(type(info))
# print(info)
