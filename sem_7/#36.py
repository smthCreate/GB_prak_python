def print_operation_table(operation, num_r=6, num_c=6):
    arrays = []
    for i in range(1, num_r + 1):
        ar = [operation(i, y) for y in range(1, num_c + 1)]
        arrays.append(ar)
    return arrays


arrays = print_operation_table(lambda x, y: x ** 2 + 2 * y)
for i in arrays:
    for j in i:
        print(' {}'.format(j), end=' ')
    print()
