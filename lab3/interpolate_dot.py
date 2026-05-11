#Lagrange polinomial

def interpolate_dot(x: float, dots: dict) -> float:
    sum = 0.0
    multiplier = 1.0
    for j in range(len(dots)):
        for i in range(len(dots)):
            if i == j:
                continue
            multiplier *= ((x - list(dots.keys())[i])/
                           (list(dots.keys())[j] - list(dots.keys())[i]))

        sum += dots[list(dots.keys())[j]] * multiplier

    return sum