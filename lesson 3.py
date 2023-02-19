from random import randint as rdi
#LAMBDA FUNCTIONS

# def calc(x):
#     return x*2
# def math(op,x):
#     print(op(x))
# math(calc,3)

def mylt(x,y):
    return x*y
# def calc(op,a,b):
#     print(op(a,b))
# calc(lambda q,w:q+w,2,3)


# list_start = [rdi(1,100) for i in range(1,11)]
# list_end = [(i,i**2) for i in list_start if i%2==0]
# print(list_start,list_end)

# file = open('numbers.txt',"r")
# data=[int(i) for i in file.read().split()]
# print(data)
#
# f = lambda q: not q%2
# print([i for i in map(f,data)])
#Filter
data = [rdi(1,100) for x in range(10)]
res = filter(lambda x:not x%2,data)
print(list(res))
