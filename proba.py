# a = "8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0"
# b = "6*(x**4) + 9*(x**3) + 3*(x**2) + 2*x = 0"
# a=a.split()
# b=b.split()
# print(a)
# print(b)
# for i in a:
#     if i=='+' or i=='=' or i=='0':
#         a.remove(i)
# for i in b:
#     if i=='+' or i=='=' or i=='0':
#         b.remove(i)
#
# print(a)
# print(b)
# from random import randint
# def counting_sort_extended(array):
#     mx = max(array)
#     mn = min(array)
#     print(f"mx,mn={mn},{mx}")
#     offset = -mn
#     counters = [0]*(mx+offset+1)
#     print(counters)
#     for i in array:
#         counters[int(i)+offset]+=1
#     index =0
#     for i in range(len(counters)):
#         for j in range(counters[i]):
#             array[index]=i-offset
#             index+=1
#
# N=10
# res_serial = [randint(0,5) for i in range(N)]
# print(res_serial)
# counting_sort_extended(res_serial)
# print(res_serial)
a = 3892
print(len(str(a)))