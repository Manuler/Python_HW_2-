# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#
#     *Пример:*
#
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

num = int(input('Введите число: '))
num_list = {}
res_list = {}
sum = 0
for i in range(1, num +1):
    num_list[i] = round((1+(1/i))**i, 3)
print(num_list)
for k in num_list:
    sum += num_list[k]
print(sum)