import random


def bubble_sort(my_list, iter_bubble=0):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):      # total - lo recorrido - 1
            iter_bubble +=1
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list, iter_bubble            # O(n)*O(n) = O(n*n) = O(n**2)


def insertion_sort(my_list, iter_insert=0):
    for index in range(1, len(my_list)):
        current_value = my_list[index] 
        while index > 0 and my_list[index - 1] > current_value:
            iter_insert +=1
            my_list[index] = my_list[index -1] 
            index -= 1 
        my_list[index] = current_value
    return my_list, iter_insert


if __name__ == '__main__':
    sort_list, iter_bubble = bubble_sort([1, 30, 10, 15, 5, 2])
    insert_list, iter_insert = insertion_sort([1, 30, 10, 15, 5, 2])
       
    print(f'Was {iter_bubble} iterations')
    print(f'Was {iter_insert} iterations')

