from interpolate_function import interpolate_function
from lab3.interpolate_function import find_knots, find_dots
from random import randint

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

def error_accuracy(p, a, b, n = 3):
    pn = interpolate_function(p, a, b, n)
    x_vals = list(pn.keys())
    error_accuracy = {}

    for x in x_vals:
        delta_n = pn[x] - interpolate_function(p, a, b, n + 1)[x]
        delta_delta_n = interpolate_function(p, a, b, n + 1)[x] - interpolate_function(p, a, b, n + 2)[x]
        error_accuracy[x] = abs(delta_delta_n / delta_n)

    return error_accuracy

def error_table(p, a, b, n = 5):
    pn = interpolate_function(p, a, b, n)
    x_vals = list(pn.keys())
    x_index = randint(0, n - 1)

    lagrange_error_ = lagrange_error(p, a, b, n)
    table_n = lagrange_error_[x_vals[x_index]]

    delta_n = pn[x_vals[x_index]] - interpolate_function(p, a, b, n + 1)[x_vals[x_index]]
    exec_delta = p(x_vals[x_index]) - interpolate_function(p, a, b, n)[x_vals[x_index]]

    k = 1 - exec_delta / delta_n
    return (f"n |n| exec_delta_n |k|\n"
            f"{n} |{table_n}| {exec_delta} |{k}|")
