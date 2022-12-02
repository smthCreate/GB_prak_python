
#1
def summ(x):
    x = list(str(x))
    print(x)
    x.remove('.')
    return sum([int(i) for i in x])

#2
def compos(n):
    answer = [1]
    while answer.index(answer[-1])<n-1:
        answer.append((answer.index(answer[-1])+2)*answer[-1])
    return answer

#3
def sum_of_order(n):
    answer = [1]
    while answer.index(answer[-1]) < n - 1:
        answer.append((answer.index(answer[-1]) + 2) * answer[-1])
    return answer

#4
def compos_of_list(str,ls):
    indexs = [int(i) for i in str.split()]
    compos = 1
    for i in indexs:
        compos*=ls[i]
    return compos
n = int(input())
ls = [i for i in range(-n,n+1)]

#5
