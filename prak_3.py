

import math
#1
def sum_1(ls):
    s = 0
    for i in range(0,len(ls),2):
        s+=ls[i]
    return s
# n= int(input())
# ls = [i for i in range(1,n+1)]

#2
def compos_of_pairs(ls):
    answer = []
    while len(ls)>0:
        answer.append(ls[0]*ls[-1])
        ls.pop(0)
        try:
            ls.pop(-1)
        except:
            pass
    return answer
#n = [int(i) for i in input().split()]

#3
def max_of_(ls):
    answer = []
    for i in ls:
        answer.append(i%1)
    return max(answer)
#n = [float(i) for i in input().split()]

#4
def binner(x):
    answer = []
    while x>0:
        answer.append(x%2)
        x//=2
    answer = [str(i) for i in answer]
    return "".join(answer)

#5
def negafib(x):
    if x ==-2:
        return -1
    elif x >=-1:
        return 1
    return negafib(x+2)-negafib(x+1)

def fibonacci(n):
    if n in (1, 2):
        return 1
    if n ==0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


def list_of_fibs(n):
    ls = []
    n=int(math.fabs(n))
    m=-n
    for i in range(m,n+1):
        if i >=0:
            ls.append(fibonacci(i))
        else:
            ls.append(negafib(i))
    return ls

print(list_of_fibs(int(input())))