from interpolate_function import find_dots
from error_calculation import exec_error, lagrange_error, error_table, min_error_accuracy
from given_function import p
from create_graph import draw_error_graph
from math import sin

from lab3.interpolate_function import interpolate_function


def main():
    errors = {}
    a, b = 0, 2
    function = find_dots(sin, a, b)

    for i in range(3, 21):
        # errors[i] = lagrange_error(sin, a, b, i)
        errors[i] = exec_error(function, interpolate_function(sin, a, b, i))

    error_values = []
    # for error in errors:
    #     error_values.append(list(errors[error].values()))
    for error in errors:
        error_values.append(errors[error])

    draw_error_graph(list(function.keys()), error_values)

    print(error_table(sin, a, b))

    print(f"Найбільша розмитість похибки: {min_error_accuracy(sin, a, b)}")

if __name__ == "__main__":
    main()
