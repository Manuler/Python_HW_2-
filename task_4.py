# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число n = '))

list_n = []
for i in range(-abs(n), abs(n)+1):
    list_n.append(i)
print(list_n)

mult = 1
path = 'task_4'
with open(path, 'r') as data:
    for line in data:
        mult *= list_n[int(line)]
    print(mult)