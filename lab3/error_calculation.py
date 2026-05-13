from interpolate_function import interpolate_function
from lab3.interpolate_function import find_knots

# Lagrange error
def knot_multiplier(x: float, xk_vals: list) -> float:
    multiplier = 1
    for i in xk_vals:
        multiplier *= (x - i)
    return multiplier

def lagrange_error(p, a, b, i = 10):
    knots1 = find_knots(p, a, b, i)
    knots2 = find_knots(p, a, b, i, True)
    p1 = interpolate_function(p, a, b, i, knots1)
    p2 = interpolate_function(p, a, b, i, knots2)

    x_vals = list(p1.keys())
    lagrange_error_values = {}

    for x in x_vals:
        p1_multiplier = knot_multiplier(x, list(knots1.keys()))
        p2_multiplier = knot_multiplier(x, list(knots2.keys()))
        error = (p1.get(x) * p2_multiplier - p2.get(x) * p1_multiplier)/(p2_multiplier - p1_multiplier)
        lagrange_error_values[x] = error

    return lagrange_error_values

def max_lagrange_error(lagrange_error_: dict):
    return max(list(lagrange_error_.values()))

def exec_error(p:dict, l: dict):
    if len(p) != len(l):
        raise ValueError('The length of p does not match the length of l')

    difference = []
    for x in list(p.keys()):
        difference.append(abs(p[x] - l[x]))

    return difference

def max_exec_error(p:dict, l: dict):
    return max(exec_error(p, l))

def error_of_error_calculation(exec_error: list, lagrange_error: dict):
    ...