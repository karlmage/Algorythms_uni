from interpolate_function import interpolate_function, find_dots
from error_calculation import max_error
from given_function import p
# from math import sin

def main():
    errors = {}
    a, b = 0, 2
    function = find_dots(p, a, b)

    for i in range(3, 10):
        interpolated_function = interpolate_function(p, a, b, i)
        errors[i] = max_error(function, interpolated_function)

    for error in errors:
        print(f"{error}: {errors[error]}")

    #error_of_error = error_of_error_calculation(p, a, b, errors)
    #if error_of_error < 1:
    #    print(f"Відносна розмитість оцінки мала і дорівнює {error_of_error}. Їй можна довіряти.")
    #else:
    #    print(f"Відносна розмитість оцінки велика і дорівнює {error_of_error}. Їй не варто вірити")

if __name__ == "__main__":
    main()
