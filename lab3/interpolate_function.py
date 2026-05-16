graph_steps_count = 120

def find_dots(p, a: int, b: int) -> dict:
    global graph_steps_count
    return find_knots(p, a, b, graph_steps_count)

def find_knots(p, a: int, b: int, i = 10, adjust = False) -> dict:
    x_vals = []
    step = float((b - a)/i)
    if adjust:
        step += step

    while a <= b:
        x_vals.append(a)
        a+=step

    dots = {}
    for k in x_vals:
        dots[k] = p(k)

    return dots

#Lagrange polinomial
def interpolate_dot(x: float, dots: dict) -> float:
    sum = 0.0
    for j in range(len(dots)):
        multiplier = 1.0
        for i in range(len(dots)):
            if i == j:
                continue
            multiplier *= ((x - list(dots.keys())[i])/
                           (list(dots.keys())[j] - list(dots.keys())[i]))

        sum += dots[list(dots.keys())[j]] * multiplier

    return sum

def interpolate_function(p, a: int, b: int, i = 10, knots = None, adjust = False) -> dict:
    global graph_steps_count
    if knots is None:
        knots = find_knots(p, a, b, i, adjust)

    interpolated_function = {}

    x_vals = []
    x = a
    step = float((b - a) / graph_steps_count)  # Визначаємо шаг відображення функції, щоб було видно похибку
    while x <= b:
        x_vals.append(x)
        x += step

    if b - x_vals[-1] > 0.1:
        x_vals.append(b)

    for i in x_vals:
        interpolated_function[i] = interpolate_dot(i, knots)

    return interpolated_function
