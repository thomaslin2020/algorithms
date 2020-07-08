def naive_multiplication(x, y):
    x, y = str(x), str(y)
    len_x, len_y = len(x), len(y)
    result, temp = 0, 0
    for i in range(len_y):
        temp = 0
        for j in range(len_x):
            temp += int(y[len_y - i - 1]) * int(x[j]) * int(10 ** (len_x - j - 1))
        result += int(10 ** i) * temp
    return result


def karatsuba(x, y):
    len_x, len_y = len(str(x)), len(str(y))
    if len_x == 1 and len_y == 1:
        return x * y
    else:
        n = max(len_x, len_y)
        nby2 = n // 2
        temp = 10 ** nby2
        a, b, c, d = x // temp, x % temp, y // temp, y % temp
        ac, bd = karatsuba(a, c), karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd
        prod = ac * 10 ** (2 * nby2) + ad_bc * 10 ** nby2 + bd
        return prod
