from interpolate_function import interpolate_function

def lagrange_error(p1, p2):
    ...

def exec_error(p:dict, l: dict):
    if len(p) != len(l):
        raise ValueError('The length of p does not match the length of l')

    difference = []
    for x in list(p.keys()):
        difference.append(abs(p[x] - l[x]))

    return difference

def max_error(p:dict, l: dict):
    return max(exec_error(p, l))

def error_of_error_calculation():
    ...