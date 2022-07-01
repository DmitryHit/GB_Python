user_input = input("Введите число: ")
variable = 0
for value in user_input:
    while int(value) > variable:
        variable = int(value)
print("Самая большая цифра в числе: ", variable)

