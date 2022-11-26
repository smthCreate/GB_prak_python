import itertools
import math as mt

#1
def holidays(x):
    if x in [6,7]:
        output = "yes"
    elif x in [1,2,3,4,5]:
        output = "no"
    else:
        output = "Not in range"
    return output

#2
def logicwork():
    all_predicts = []
    for i in itertools.combinations_with_replacement("010",3):
        i = list(i)
        for j in range(len(i)):
            i[j] = int(i[j])
        all_predicts.append(i)
    answer = str()
    for i in all_predicts:
        if ((-1)*(i[0]*i[1]*[2]))==((-1)*i[0]+(-1)*i[1]+(-1)*i[1]):
            if answer != "no":
                answer = "yes"
        else:
            answer = "no"
    return answer

#3
def quarter_out (x,y):
    quarters = [1,2,3,4]
    if x*y>0:
        if x>0:
            return quarters[0]
        else:
            return quarters[2]
    else:
        if x>0:
            return quarters[3]
        else:
            return quarters[1]

#4
def quarter_in(x):
    quarters = [1, 2, 3, 4]
    answer = str()
    if x == quarters[0]:
        answer = "x>0,y>0"
    elif x == quarters[1]:
        answer =  "x<0,y>0"
    elif x == quarters[2]:
        answer =  "x<0,y<0"
    elif x not in quarters:
        answer = "wow,wow, input quarter number, pls"
    else:
        answer =  "x>0,y<0"
    return answer

#5
def distance(x):
    x = x.split(" ")
    point1 = [ int(list(x[1])[1]), int(list(x[1])[3])]
    point2 = [int(list(x[3])[1]), int(list(x[3])[3])]
    distance_between = mt.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    return round(distance_between,3)

