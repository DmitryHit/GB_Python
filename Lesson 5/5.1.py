user_text = []

while True:
    text = input('Вводите текст для сохранения в файл: ')
    if text == '':
        break
    else:
        addtext = text + '\n'
        user_text.append(addtext)

    with open('5.1.txt', 'w', encoding='utf-8') as file:
        file.writelines(user_text)


