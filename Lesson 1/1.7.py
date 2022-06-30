result = int(input("Введите результаты пробежки первого дня в км: "))
desired_result = int(input("Введите общий желаемый результат в км: "))
day = 1
print("Результат:")
print(day, "-й день:", result)
while desired_result - result > 0:
    result = result + (result * 0.1)
    day += 1
    print(day, "-й день:", round(result, 2))
print("Вы достигнете результата на", day, "-й день!")
