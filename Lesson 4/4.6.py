from itertools import cycle as cy, count as co

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stop = 0


for el in co(3):
    print(el)
    if el > 10 - 1:
        break


for i in cy(data):
    if stop < 100:
        print(i)
        stop += 1
    else:
        break
