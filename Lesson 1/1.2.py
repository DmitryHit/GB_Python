user_input = int(input("Введите время в секундах: "))
hours = (user_input//3600) % 24
minutes = (user_input//60) % 60
seconds = user_input % 60

print('%02d:%02d:%02d ' % (hours, minutes, seconds))
