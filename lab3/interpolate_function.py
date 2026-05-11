from find_dots import find_dots
from interpolate_dot import interpolate_dot

def interpolate_function(i: int, a: float, b: float, p):
    dots = find_dots(i, a, b, p)
    interpolated_function = {}

    for i in dots.keys():
        interpolated_function[i] = interpolate_dot(i, dots)

    return interpolated_function
