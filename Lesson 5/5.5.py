from random import randint as ri
sum_num = 0
with open('5.5.txt', 'w+', encoding='utf-8') as file:

    for num in (ri(1, 100) for el in range(10)):
        file.write(str(num) + ' ')
        sum_num += num

print(sum_num)
