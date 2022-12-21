from random import randint as rd
import math as mt
#1
def rounder(n):
    round_to = len(str(n))-2
    return round(mt.pi,round_to)

#2
def ls_of_comp(n):
    ls = []
    x=1
    while x<n+1:
        if n%x==0:
            ls.append(x)
        x+=1
    return ls

#3
def do_not_repeat(ls):
    ls_to_return = []
    for i in ls:
        if ls.count(i)==1:
            ls_to_return.append(i)
    return ls_to_return

#4
def polynom(k):
    koefs = [rd(0,100) for i in range(k+1)]
    result = [0 for i in range(k+1)]
    for i in range(k):
        j=k-i
        if koefs[i]!=0:
            result[i]=f'{koefs[i]}*(x**{j})+'
    result[-1]=koefs[-1]
    result.append('=0')
    return ''.join([str(i) for i in result])

#5

def formating(f1):
    f1_n = []
    for i in f1:
        if i!='+' and i!="=":
            ls=list(i)
            ls2=[]
            for c in ls:
                if c != "*" and c != "(" and c != ")":
                    ls2.append(c)
            if len(ls2)==1:
                ls2.append(0)
            elif len(ls2)==2:
                ls2.pop(-1)
                ls2.append(1)
            else:
                ls2.remove('x')
            f1_n.append([int(i) for i in ls2])
    return f1_n

def plus(f1,f2):
    f1=formating(f1)
    f2=formating(f2)
    result = []
    for i in f1:
        for j in f2:
            if i[1]==j[1]:
                i[0]+=j[0]
        result.append(f"{i[0]}x**{i[1]}")
        result.append("+")
    result.pop(-1)
    result.append("=0")
    return " ".join(result)
f1 = [i for i in open("polyno_1.txt",'r').read().split()]
f2 = [i for i in open("polyno_2.txt",'r').read().split()]
f1.pop(-1)
f2.pop(-1)
print(plus(f1,f2))


