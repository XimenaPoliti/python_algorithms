import random


def linear_search(my_list, value, iter_lin=0):
    match = False
    for e in my_list:
        iter_lin+=1
        if e == value:
            match = True
            break
    return (match, iter_lin)


def binary_search(my_list, start, end, value, iter_bin=0):
    iter_bin+=1
    if start > end:
        return (False, iter_bin)

    middle = (start + end) // 2

    if my_list[middle] == value:
        return (True, iter_bin)
    elif my_list[middle] < value:
        return binary_search(my_list, middle + 1, end, value, iter_bin=iter_bin)
    else:
        return binary_search(my_list, start, middle - 1, value, iter_bin=iter_bin)


if __name__ == '__main__':
    len_list = int(input('Enter list size: '))
    value = int(input('Enter value: '))
    
    my_list = sorted([random.randint(0, 100) for i in range(len_list)])
    match_binary, iter_bin = binary_search(my_list, 0, len(my_list), value)
    match_linear, iter_lin = linear_search(my_list, value)

    print(my_list)
    print(f'The value {value} {"is on" if match_linear else "not on"} the list, iterations linear search: {iter_lin}')
    print(f'The value {value} {"is on" if match_binary else "not on"} the list, iterations binary search: {iter_bin}')
