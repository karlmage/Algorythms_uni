def find_dots(i: int, a: float, b: float, p) -> dict:
    x_vals = []
    step = float((b-a)/i)

    x_vals.append(a)

    while a < b:
        a+=step
        x_vals.append(a)

    dots = {}
    for i in x_vals:
        dots[i] = p(i)

    return dots