def find_dots(p, a: int, b: int, i = 10 ) -> dict:
    x_vals = []
    step = float((b - a)/(i * 4))

    x_vals.append(a)

    while a <= b:
        x_vals.append(a)
        a+=step

    dots = {}
    for i in x_vals:
        dots[i] = p(i)

    return dots

def find_knots(p, a: int, b: int, i = 10 ) -> dict:
    x_vals = []
    step = float((b - a)/i)

    while a <= b:
        x_vals.append(a)
        a+=step

    dots = {}
    for i in x_vals:
        dots[i] = p(i)

    return dots