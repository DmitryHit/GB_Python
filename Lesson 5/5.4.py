numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('5.4.txt', 'r') as file:
    for el in file:
        el = el.split(' ', 1)
        new_file.append(numerals[el[0]] + '  ' + el[1])
    print(new_file)

with open('5.4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
