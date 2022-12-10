import random


def bubble_sort(my_list, iter_bubble=0):
    n = len(my_list)

    for i in range(n):
        for j in range(0, n - i - 1):      # total - lo recorrido - 1
            iter_bubble +=1
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list, iter_bubble            # O(n)*O(n) = O(n*n) = O(n**2)


if __name__ == '__main__':
    len_list = int(input('Enter list size: '))
    my_list = [random.randint(0, 100) for i in range(len_list)]
    print(my_list)
    sort_list, iter_bubble = bubble_sort(my_list)
    print(sort_list)
    print(f'Was {iter_bubble} iterations')
