user_input = [i for i in input("Введите элементы списка через пробел:").split()]
for i in range(1, len(user_input), 2):
    user_input[i - 1], user_input[i] = user_input[i], user_input[i - 1]
print(' '.join([str(i) for i in user_input]))
