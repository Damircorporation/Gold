# Задача №1 - Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# РЕШЕНИЕ
# list_1 = [1, 3, 3, 4, 5]
# k = 3
# print(list_1.count(k))

# не решена до конца
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# temp = 0
# for _ in range(len(list_1)):
#     if i == k:
#         temp += 1
# else:
#     i+=1
# print(temp)



# Задача №2 - Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
# РЕШЕНИЕ
# list_1 = [1, 2, 2, 2, 5, 9, 5, 1, 2, 7]
# k = 4
# def closest(list_1, k):  
#     return list_1[min(range(len(list_1)), key = lambda i: 
#                       abs(list_1[i]-k))]
# print(closest(list_1, k))

# или так

# items = [1,2,3,4,5] # список чисел
# value = 2.2         # число к которому найти ближайшее
# def nearest_value(items, value):
#     '''Поиск ближайшего значения до value в списке items'''
#     found = items[0]        # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
#     for item in items:      # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
#         # проверяем условие если разница между item value по модулю меньше разницы found и value, то
#         if abs(item - value) < abs(found - value): # если условие истинно (True)
#             found = item # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
#     return found # возвращаем ближайшее значение до value в списке items
# print(f'Ближайшее число к {value} в списке {items} является {nearest_value(items, value)}')



# Задача №3 - Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# РЕШЕНИЕ
# scrable = {
# 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'А': 1, 'В': 1, 'Е': 1,
# 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2, 'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2,
# 'У': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4,
# 'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4, 'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8, 'X': 8, 'Ш': 8,
# 'Э': 8, 'Ю': 8, 'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
# word = str.upper(input('Введите слово: '))
# s = 0
# for i in word:
#     s += scrable[i]
# print(s, 'очков')

# нужный словарь

# 'н': 1, 'о': 1, 'у': 1, 'т': 1, 'б': 3, 'к': 4, 'я': 1, 'щ': 1, 'е': 2, 'р': 2, 'и': 6, 'ц': 5, 'а': 5,
# 'l': 1, 'a': 1, 'p': 1, 't': 3, 'o': 3, 'i': 1, 'z': 1, 'r': 6, 'd': 6}