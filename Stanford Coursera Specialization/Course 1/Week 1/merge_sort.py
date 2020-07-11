# random array
import random

start, stop, limit = 1, 100, 100
num = [random.randrange(start, stop) for _ in range(limit)]


def merge(a, b, n):
    # merges two sorted arrays into array of len n
    o = []
    i, j, len_a, len_b = 0, 0, len(a), len(b)
    for k in range(n):
        if a[i] < b[j]:
            o.append(a[i])
            i += 1
        else:
            o.append(b[j])
            j += 1
        if i == len_a:
            return o + b[j:]
        elif j == len_b:
            return o + a[i:]
    return o


def merge_sort(o):
    len_o = len(o)
    if len_o > 1:
        m = len_o // 2
        l, r = o[:m], o[m:]
        return merge(merge_sort(l), merge_sort(r), len_o)
    else:
        return o


print(merge_sort(num))
