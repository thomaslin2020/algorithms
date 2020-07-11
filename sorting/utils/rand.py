import random


def random_int_array(start, stop, limit):
    return [random.randrange(start, stop) for _ in range(limit)]
