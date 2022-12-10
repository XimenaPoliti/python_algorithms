import random


def linear_search(my_list, value):
    match = False
    for i in my_list:        #O(n)
        if i == value:
            match = True
            break
    return match

if __name__ == '__main__':
    len_list = int(input('Enter list size: '))
    value = int(input('Enter value: '))
    my_list = [random.randint(0, 100) for i in range(len_list)]
    match = linear_search(my_list, value)
    print(my_list)
    print(f'The value {value} {"is on" if match else "not on"} the list')

    
