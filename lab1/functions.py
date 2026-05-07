from math import pow, factorial

def linear(a: int, c: int) -> float:
    if not a.is_integer() or not c.is_integer():
        raise TypeError("Input values are not integers.")
    if a < c:
        raise ValueError("a value must be bigger than c.")

    z = (pow(a, 2) - pow(c, 2)) / 7
    d = factorial(a) / (factorial(c) * factorial(a - c))
    y1 = z + d
    return int(y1)

def branched(x:int, k:int, c:int, b:int) -> float:
    if (not x.is_integer() or not k.is_integer() or
            not c.is_integer() or not b.is_integer()):
        raise TypeError("Input values are not integers.")

    if x > 0:
        y = k * pow(x, 2) + c * x + b
    else:
        y = b * pow(x, 2) + c * x + k
    return int(y)

def cyclical(a:list[int], n:int) -> float:
    if not n.is_integer():
        raise TypeError("Input values are not integers.")
    for i in a:
        if not i.is_integer():
            raise TypeError("Input values are not integers.")

    if n == 0:
        return 0
    if len(a) == 0 or len(a) < n:
        print ("The list is empty or too short.")
        return 1

    f = 0
    i_f = 1

    for i in range(n):
        for j in range(n):
            i_f *= a[i-1] + pow(a[j-1], 2)
        f += i_f

    return f