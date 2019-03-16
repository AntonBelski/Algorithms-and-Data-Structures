# Merge Sort (Сортировка вставками)


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    left = merge_sort(array[:n // 2])
    right = merge_sort(array[n // 2:])
    return merge_arrays(left, right)


def merge_arrays(array1, array2):
    result = []
    len_a1 = len(array1)
    len_a2 = len(array2)
    l = 0
    r = 0
    while l < len_a1 or r < len_a2:
        if l == len_a1 or (r < len_a2 and array1[l] > array2[r]):
            result.append(array2[r])
            r = r + 1
        else:
            result.append(array1[l])
            l = l + 1
    return result
