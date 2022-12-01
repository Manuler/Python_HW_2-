# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)
#
#     *Пример:*
#
#     - 6782 -> 23
#     - 0,56 -> 11

# num = float(input('Введите число: '))
# while num % 1 != 0:
#     num *=10
# print(int(num))
# sum = 0
# while num > 0:
#     last = num % 10
#     sum += last
#     num //= 10
# print(int(sum))

num = input('Введите число: ')
sum = 0
for i in num:
    if i.isdigit():
        sum += int(i)
print(f'Сумма цифр{num} равна {sum}')