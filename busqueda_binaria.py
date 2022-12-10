import random


def binary_search(my_list, start, end, value):  # O(log n)
    print(f'La búsqueda de {value} se da entre {start} y {end}')
    if start > end:
        return False
    middle = (start + end) // 2
    if my_list[middle] == value:
        return True
    elif my_list[middle] < value:
        return binary_search(my_list, middle + 1, end, value)
    else:
        return binary_search(my_list, start, middle - 1, value)


if __name__ == '__main__':
    len_list = int(input('Enter list size: '))
    value = int(input('Enter value: '))
    my_list = sorted([random.randint(0, 100) for i in range(len_list)])
    match = binary_search(my_list, 0, len(my_list), value)
    print(my_list)
    print(f'The value {value} {"is on" if match else "not on"} the list')
