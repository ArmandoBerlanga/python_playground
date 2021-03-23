# Creado por José Armando Berlanga Mendoza
# Creado el 17 de febrero de 2021
# Objetivo: practicar algoritmos de ordenamiento

def selection_sort (nums : list):
    
    for i in range (len(nums)):
        min = i

        for j in range (i, len(nums)):
            if (nums[j] < nums[min] if type else nums[j] > nums[min]):
                min = j

        swap(nums, i, min)


def insertion_sort (nums : list, action : bool): # mueve el mas chico/grande a su lugar y los compara con su adyacente izq; si no cumple no compara y sigue con el siguiente num (i)
    
    for i in range (1, len(nums)):
        j = i
        while (j != 0 and nums[j] < nums [j-1] if action else nums[j] > nums [j-1]):
            swap (nums, j, j-1)
            j -= 1


def bubble_sort (nums : list, j : int, type : bool): # compara en pares con su adyacente derecho y mueve y mueve el mas grande/chico hasta la derecha
    
    if j == len(nums):
        return 1

    else:
        for k in range (len(nums)-1-j):
            if (nums[k] > nums [k+1] if type else nums[k] < nums [k+1]):
                swap(nums, k, k+1)

        j += 1
        return bubble_sort(nums, j, type)


def quick_sort (nums : list, inicio : int, fin : int):

    if inicio < fin:
        particion = obtener_particion(nums, inicio, fin)
        quick_sort (nums, particion+1, fin)
        quick_sort (nums, inicio, particion-1)


def obtener_particion (nums : list, inicio : int, fin : int):

    pivote = nums [fin]
    curr = inicio-1

    for i in range (inicio, fin):
        # print (nums)
        if nums[i] < pivote:
            curr+=1
            swap(nums, i, curr)

    swap (nums, curr+1, fin)
    return curr+1


def swap (nums : list, i : int, j : int):
    
    saved = nums [j]
    nums [j] = nums [i]
    nums [i] = saved