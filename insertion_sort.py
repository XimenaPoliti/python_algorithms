def insertion_sort(my_list, iter_insert=0):
    for index in range(1, len(my_list)):
        current_value = my_list[index]
        while index > 0 and my_list[index - 1] > current_value:
            iter_insert +=1
            my_list[index] = my_list[index -1]
            index -= 1
        my_list[index] = current_value
    return my_list, iter_insert       
    
    

if __name__=='__main__':
    my_list = [7,5,3,8,1,9,8,2]
    list_sort = insertion_sort(my_list)
    print(list_sort)
