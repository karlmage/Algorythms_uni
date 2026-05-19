def derivative(f, x):
    ...

def newton_raphson_method(f, e, a: int, b: int):
    while True:
        if f(a) * f(b) < 0:
            print("Введіть нові значення a і b або q, щоб вийти")
            a = input("a: ")
            if a == "q":
                return 0
            b = input("b: ")
            if b == "q":
                return 0
        else:
            break

    k = 0
    if abs(b - a) > e:
        x = (a + b) / 2
        return x, k

    ...

