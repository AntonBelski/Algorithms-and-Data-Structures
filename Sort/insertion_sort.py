# Insertion sort


def insert_sort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j = j - 1
    return array
