# # 1 Задайте список из нескольких чисел. 
# #Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
# size = int(input('Введите размер списка '))
# list = []
# for i in range(size):
#     list.append(randint(0, 9))
# print(list)
# def search(size):
#     result = 0
#     for i in range(len(size)):
#         if i%2 == 1:
#             result +=size[i]
#     return result
# print(search(list))           

# # 2 Напишите программу, которая найдёт произведение пар чисел списка.
# #  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# size = int(input('Введите размер списка '))
# list = []
# list2 = []
# for i in range(size):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and size > len(list)/2:
#         size = size - 1
#         a = list[i] * list[size]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)

#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# import random 
# size = int(input('Введите размер списка '))
# list = []
# for i in range(size):
#     list.append(random.uniform(-10, 10))
# print(list)
# new_list = [(i%1) for i in list]
# print(new_list)
# print(max(new_list) - min(new_list))

# #4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# n = int(input('Введите число '))
# result = ""
# while n != 0:
#     result = str(n%2) + result
#     n //=2
# print(result)

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число: '))
list = []
if k>0:
    list = [1, 0, 1]
for i in range(k):
    list.append(list[len(list)-1]+list[len(list)-2])
    if k%2==0:
        list.insert(0, list[len(list)-1])
    else:
        list.insert(0, list[len(list)-1])
print(list)