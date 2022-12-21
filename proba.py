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
a='8*(x**4)'
a=list(a)
print(a)
b=[]
for c in a:
    if c == '*' or c == "(" or c == ")":
        a.remove(c)
    else:
        b.append(c)
print(a)
print(b)