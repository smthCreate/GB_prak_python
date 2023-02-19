from random import randint as rd
from math import pi
#filter
# ls1 = [1,2,3,45,66,88]
# print(list(filter(lambda x:x%2==0,ls1)))

# zip
# ls1 = [1,2,3]
# ls2 = ["Tom",'Tommy',"Thomas"]
# ls3 = [True,False,True]
# print(list(zip(ls1,ls2)))

# orn = [(1,2),(1,2)]
# print(*orn)

#47
# transformation = lambda x: x**2
# values = [i+rd(1,3) for i in range(1,20)]
# transformed_values = list(map(transformation,values))
# print(values,'\n',transformed_values,len(values)==len(transformed_values))

#49
orbits = [(123,234),(456,382),(2149,2321)]

# def find_orbist(orbits):
#     for elem in orbits:
#         if str(elem[0]).isdigit() and str(elem[1]).isdigit() and elem[0]>0 and elem[1]>0:
#             continue
#         else:
#             print("Введите только числа!")
#             exit()
#     maxy =0
#     kort = ()
#     for elem in orbits:
#         if elem[0]==elem[1]:
#             continue
#         s = pi*elem[0]*elem[1]
#         if s>maxy:
#             maxy=s
#             kort = elem
#     return kort
# print(find_orbist(orbits))