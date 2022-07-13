import re
schedule = {}
with open('5.6.txt', encoding='utf-8') as file:

    for el in file.readlines():
        subject = el.split(':')[0]
        lessons = 0

        for x in re.findall('\d+', el):
            lessons += int(x)
        schedule.update({subject: lessons})

print(schedule)
