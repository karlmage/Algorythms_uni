from random import randint
from timeit import repeat

def generate_array(array_length = 1000):
    return [randint(0, 1000) for i in range(array_length)]

def run_sorting_algorithm(algorithm, array):
    stmt = lambda: algorithm(array)

    times = repeat(stmt = stmt, number = 10)

    return f"Algorithm: {algorithm.__name__}. Array length: {len(array)}. Minimum execution time: {min(times)}"

if __name__ == "__main__":
    from quicksort import quicksort

    run_sorting_algorithm(quicksort, generate_array())