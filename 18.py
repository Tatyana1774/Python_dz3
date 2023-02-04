# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
#-> 5

# l = input('Введите значение N: ')
# numbers = list(map(int, input('Введите через пробел числа: ').strip().split()))
# x = int(input('Введите X: ').strip())

# res = numbers[0]
# for i in numbers:
#     if abs(i - x) < abs(res - x):
#         res = i
# print(res)

#2 ррешение
n=[int(i) for i in input('Введите значение N: ').split()]
x=int(input('Введите значение X: '))
number=0
for i in range(len(n)):
    if (x-n[i])<x-number and x-n[i]>0:
        number=i
print(n[number])