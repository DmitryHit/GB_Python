num_lines = 0
with open('5.2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = len(line.split())

        num_lines += 1
        print(f'Строка № {num_lines}: Кол-во слов в строке - {words}')
