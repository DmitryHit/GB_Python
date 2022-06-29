user_str = input("Введите текс: ")
temp = user_str.split(' ')
for i, user_str in enumerate(temp, 1):
    if len(user_str) > 10:
        user_str = user_str[0:10]
    print(f"{i}. - {user_str}")
