from find_dots import find_dots
from interpolate_function import interpolate_function
from error_calculation import max_error
from given_function import p

errors = {}
a, b = 0, 2

for i in range(3, 11):
    function = find_dots(p, a, b, i)
    interpolated_function = interpolate_function(p, a, b, i)
    errors[i] = max_error(function, interpolated_function)

for error in errors:
    print(f"{error}: {errors[error]}")