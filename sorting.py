import random
from timeit import repeat
import math
from sorting import (
    mergesort_iterative,
    mergesort_recursive,
    quicksort_inplace,
    quicksort_recursive,
    insertionsort,
    bubblesort,
    selectionsort,
)


ARRAY_LENGTH = 10000


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    random.seed(2001)
    array = [random.randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # array = list(range(10000))
    # run_sorting_algorithm(algorithm="sorted", array=array)
    # run_sorting_algorithm(algorithm="bubblesort", array=array)
    # run_sorting_algorithm(algorithm="selectionsort", array=array)
    random.shuffle(array)
    print(mergesort_iterative(array.copy()) == quicksort_inplace(array.copy()))
    run_sorting_algorithm(algorithm="sorted", array=array.copy())
    run_sorting_algorithm(algorithm="mergesort_recursive", array=array.copy())
    run_sorting_algorithm(algorithm="mergesort_iterative", array=array.copy())
    run_sorting_algorithm(algorithm="quicksort_recursive", array=array.copy())
    run_sorting_algorithm(algorithm="quicksort_inplace", array=array.copy())
