def main():
    my_list = read_data()
    write_data(my_list)
    operations = [[1, "Number search", lambda: search_data(my_list)],
                  [2, "Print whole book", lambda: print_data(my_list)],
                  [3, "Add to book", lambda: add_user(my_list)],
                  [4, "Change number in the book", lambda: change_book(my_list)],
                  [5, "Delete number from the book", lambda: removal(my_list)], [6, "End work", lambda: exit()]]
    choice = menu(operations)
    while choice != (operations[-1][0] + 1):
        operations[choice - 1][2]()
        choice = menu(operations)


def menu(operations):
    leng = max([len(i[1]) for i in operations])
    print("Select one of the following menu items")
    for i in operations:
        print("|{}".format(i[0]) + "|{}".format(i[1]) + " " * (leng - len(i[1])))
    return i_input()


def i_input():
    while True:
        try:
            move = int(input("Input your choice: "))

        except ValueError:
            print("Please! Input correct number!")
            continue
        break
    return move


def removal(my_list):
    check = True
    while check:
        rem = input("Input user to delete: ")
        print("There are all entries that will be deleted:")
        result = search_data(my_list, rem)
        print("Are you sure to delete all these entries?(print 'yes' or 'no')")
        answer = input()
        if answer == 'yes':
            for i in result:
                my_list.pop(i[1])
            print("Inputs were deleted!")
            check = False
        elif answer == 'no':
            print("Repeat please with more details")
        elif answer != 'yes' and answer != 'no':
            print("Repeat please with correct answer")


def change_book(my_list):
    old_u = input("Input user to change: ")
    new_u = input("Input new data of user: ")
    print("There are all string that will be changed:")
    result = search_data(my_list, old_u)

    for i in result:
        my_list[i[1]] = new_u
    print("Inputs were changed!")


def read_data():
    with open('C:\\Users\\user\\PycharmProjects\\GB_prak_python\\sem_8\\phone_book\\data.txt', 'r',
              encoding='utf-8') as file:
        my_list = file.readlines()
        return my_list


def print_data(my_list):
    for i in my_list:
        print(i.strip())


def add_user(my_list):
    my_list.append('\n' + input("Add user: "))
    print("User added")


def write_data(my_list):
    with open('C:\\Users\\user\\PycharmProjects\\GB_prak_python\\sem_8\\phone_book\\data1.txt', 'w',
              encoding='utf-8') as file:
        file.writelines(my_list)


def search_data(my_list, text=None):
    if text == None:
        text = input('Input data to find: ')
    result = []
    for i in range(len(my_list)):
        if text in my_list[i]:
            result.append([my_list[i].strip(), i])
    print([i[0] for i in result])
    return result


main()
