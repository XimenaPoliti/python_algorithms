import random

def merge_sort(my_list):
    if len(my_list) > 1:
        middle = len(my_list) // 2
        left = my_list[:middle]
        right = my_list[middle:]
        print(left, '*' * 5, right)

        # llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k +=1
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
        print(f'izquierda {left}, derecha {right}')
        print(my_list)
        print('-' * 50)

    return my_list


def ordenamiento_por_mezcla(lista):
    mid = len(lista)//2
    if len(lista) > 1:
        L = lista[:mid]
        R = lista[mid:]
        print(L, '*' * 5, R)
        lista.clear()

        ordenamiento_por_mezcla(L)
        ordenamiento_por_mezcla(R)
        print(f'izquierda {L}, derecha {R}')


        while len(L) > 0 and len(R) > 0:
            if L[0] < R[0]:
                lista.append(L.pop(0))
            else:
                lista.append(R.pop(0))

        while len(L) > 0:
            lista.append(L.pop(0))
        while len(R) > 0:
            lista.append(R.pop(0))

        print(lista)
        print('-' * 50)
    return lista


if __name__ == '__main__':
    len_list = int(input('Enter list size: '))
    my_list = [random.randint(0, 100) for i in range(len_list)]
    print(my_list)
    print('-' * 20)

    list_sort = merge_sort(my_list)
    print(list_sort)
