from random import randint as ri
#1
def deleter(x):
    x=list(x.split())
    for i in x:
        if "абв" in i:
            x.remove(i)
    return x

#2
#against human
candies = 2021
turn  = ri(-1,1)
while candies >28:
    if turn == 1:
        print("First player's turn!")
    else:
        print("Second player's turn!")
    print()
    ded = int(input())
    while ded>28:
        print("Don't take so much!!!")
        print()
        ded = int(input())
    candies-=ded
    turn*=-1
if turn == 1:
    print("First player wins!")
else:
    print("Second player wins!")

#aginst bot
candies = 2021
turn  = ri(-1,1)
if turn == 1:
    print("It's your first turn, human!")
else:
    print("Haha, first turn is mine!!!")
while candies >28:
    if turn == 1:
        ded = int(input())
        while ded > 28:
            print("Don't take so much!!!")
            print()
            ded = int(input())
        candies -= ded
        turn *= -1
    else:
        if candies%28!=0:#Не уверена, что он стал от этого сильно умнее, но какой-то алгоритм я ему задала)
            candies-=28
        else:
            candies-=1
if turn == 1:
    print("It's your win, human!")
else:
    print("Haha, win is mine!!!")

#3
#against human
def game():
    field_for_image = [1,2,3,4,5,6,7,8,9]
    field = [" " for i in range(9)]
    turn = 1
    first_moves = list()
    second_moves = list()
    first_el = "X"
    second_el = "O"
    print("This is your field! You need to choose a number of cell to fill it.\nX-player's turn!")
    image_field(field_for_image)
    while victory(first_moves, second_moves)==False:
        if len(first_moves)==5:
            print("It's Draw!")
            exit()
        move = i_input(field)
        if turn == 1:
            first_moves.append(move)
            field[move-1],field_for_image[move-1]=first_el,first_el
            turn = 0
            image_field(field_for_image)

        else:
            second_moves.append(move)
            field[move - 1], field_for_image[move - 1]=second_el,second_el
            turn = 1
            image_field(field_for_image)


def victory(first_moves,second_moves):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    if len(first_moves)>=3:
        for i in solution:
            if all(j in first_moves for j in i):
                print("First wins!")
                return True
            elif all(j in second_moves for j in i):
                print("Second wins!")
                return True
        return False
    else:
        return False

def i_input(field):
    while True:
        try:
            move = int(input("Input your choice: "))

        except ValueError:
            print("Please! Input correct number!")
            continue

        if move < 1 or move > 9:
            print("Invalid Input!!! Try Again")
            continue

        if field[move - 1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue
        break
    return move


def image_field(field):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(field[0], field[1], field[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(field[3], field[4], field[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(field[6], field[7], field[8]))
    print("\t     |     |")

game()


#4
def rle_module(data):
    if any(map(str.isdigit, data))== True:
        result = rle_decode(data)
    else:
        result = rle_encode(data)
    return result

def rle_encode(data):
    prev_char = ''
    count = 1
    result = ''

    if not data: return ''

    for ch in data:
        if ch != prev_char:
            if prev_char:
                result +=str(count)+prev_char
            count = 1
            prev_char = ch
        else:
            count+=1

    else:
        result+=str(count) + prev_char
        return result


def rle_decode(data):
    count = ''
    result = ''

    for ch in data:
        if ch.isdigit():
            count+=str(ch)
        else:
            result+=ch*int(count)
            count = ''

    return result


print(rle_module(input()))

