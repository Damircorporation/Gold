# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# РЕШЕНИЕ
# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# def power(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * power(a, b - 1))
# print(f'{b}-я cтепень числа {a} равна:', power(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
# *Пример:* 2 ; 2 ; 4
# РЕШЕНИЕ
# a = int(input('Введите 1-ое неотрицательное число: '))
# b = int(input('Введите 2-ое неотрицательное число: '))
# def recursive_summ(a, b):
#     if a == 0:
#         return b
#     else:
#         return recursive_summ(a -1, b + 1)
# print(recursive_summ(a, b))

