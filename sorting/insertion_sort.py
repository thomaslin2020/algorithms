from sorting.utils.rand import random_int_array


def insertion_sort(o):
    for i in range(1, len(o)):
        key = o[i]
        j = i - 1
        while j >= 0 and key < o[j]:
            o[j + 1] = o[j]
            j -= 1
        o[j + 1] = key
    return o


print(insertion_sort(random_int_array(1, 100, 100)))
