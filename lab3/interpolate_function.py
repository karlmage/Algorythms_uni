from find_dots import find_dots
from interpolate_dot import interpolate_dot

def interpolate_function(p, a: int, b: int, i = 10):
    dots = find_dots(i, a, b, p)
    interpolated_function = {}

    x_vals = []
    x = a
    step = float((b - a) / (i * 4))  # Визначаємо шаг відображення функції, щоб було видно похибку
    while (x <= b):
        x_vals.append(x)
        x += step

    for i in x_vals:
        interpolated_function[i] = interpolate_dot(i, dots)

    return interpolated_function
