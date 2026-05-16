from interpolate_function import find_dots
from error_calculation import exec_error, error_table, max_error_accuracy
from given_function import p
from create_graph import draw_error_graph
from math import sin

from lab3.interpolate_function import interpolate_function


def main(func):
    errors = {}
    a, b = 0, 2
    function = find_dots(func, a, b)

    for i in range(30, 31):
        errors[i] = exec_error(function, interpolate_function(func, a, b, i, None, False))

    error_values = []
    for error in errors:
        error_values.append(errors[error])

    draw_error_graph(list(function.keys()), error_values)

    print(error_table(func, a, b))

    print(f"Найбільша розмитість похибки: {max_error_accuracy(func, a, b)}")

if __name__ == "__main__":
    main(p)
