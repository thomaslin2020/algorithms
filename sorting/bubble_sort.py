from sorting.utils.rand import random_int_array


def bubble_sort(o):
    for i in range(len(o)):
        for j in range(i, len(o)):
            if o[j] < o[i]:
                o[i], o[j] = o[j], o[i]
    return o


print(bubble_sort(random_int_array(1, 100, 100)))
