#1
# def sequence(first_element,difference,numbers):
#     res = []
#     for i in range(1,numbers):
#         res.append(first_element+(i-1)*difference)
#     return res
#
# first_element = int(input("Введите первый член прогрессии: "))
# difference = int(input("Введите разность эелементов: "))
# numbers = int(input("Введите количество элементов последовательности: "))
# print(sequence(first_element,difference,numbers))

#2
# from random import randint
# rnge = [ int(i) for i in input("Введите миниму и максимум через пробел: ").split()]
# mn = min(rnge)
# mx = max(rnge)
#
# lst = [randint(1,100) for i in range(randint(10,25))]
# res =[]
# for i in range(len(lst)):
#     if mn<=i<=mx:
#         res.append(lst[i])
# print(len(lst),res)