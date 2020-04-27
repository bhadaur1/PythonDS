from random import randint, shuffle
from timeit import repeat
import math

ARRAY_LENGTH = 10000


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(array):
    n = len(array)
    # print(array)
    for i in range(n):
        already_sorted = True
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                already_sorted = False
                # print(array)
        if already_sorted:
            break

    return array


def selection_sort(array):
    """
    In each iteration, find the min of array[lo:hi+1]
    and swap with array[lo], then increment lo
    Invariant: everything to the left of lo is sorted
    """
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        minval = array[lo]
        minindx = lo
        for curr in range(lo + 1, hi + 1):
            if array[curr] < minval:
                minval = array[curr]
                minindx = curr
        array[lo], array[minindx] = array[minindx], array[lo]
        # print(array)
        lo += 1
    return array


def insertion_sort(array):
    """
    In a given iteration:
        1. swap array[lo] with each larger entry to the left.
        2. Increment lo pointer
    """
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        curr = lo
        while curr - 1 >= 0:
            if array[curr] < array[curr - 1]:
                array[curr], array[curr - 1] = array[curr - 1], array[curr]
            curr -= 1
        lo += 1
    return array


def mergesort_recursive(array):
    """
    Recursively divide and merge sorted sub-arrays
    """
    if len(array) == 1:
        return array
    lo = 0
    hi = len(array) - 1
    mid = (lo + hi) // 2

    array1 = mergesort_recursive(array[: mid + 1])
    array2 = mergesort_recursive(array[mid + 1 :])

    return __merge2sorted__(array1, array2)


def mergesort_iterative(array):
    """
    Start with merging adjacent subarrays of size 1
    In each iteration, double the size.
    """
    # return nextpower of 2 gt the len(array)
    # nsubmax = 2**math.ceil(math.log2(len(array)))
    s = 1
    while s < len(array):
        # print(f"Merging sorted sub arrays of size {s}")
        i = 0
        while i < len(array):
            # print(f"merge {array[i:i+s]} and {array[i+s:i+2*s]}")
            array[i : i + 2 * s] = __merge2sorted__(
                array[i : i + s], array[i + s : i + 2 * s]
            )
            i = i + 2 * s
        # print(array)
        s = s * 2
    return array


def quicksort_recursive(array):
    """
    Pick a random element as pivot
    """
    if len(array) < 2:
        return array

    # shuffle(array)
    pivotindx = randint(0, len(array) - 1)

    less = []
    same = []
    more = []
    for val in array:
        if val < array[pivotindx]:
            less.append(val)
        elif val > array[pivotindx]:
            more.append(val)
        else:
            same.append(val)
    return quicksort_recursive(less) + same + quicksort_recursive(more)


def __merge2sorted__(array1, array2):
    """
    Takes two sorted sub-arrays and returns a sorted array
    """
    m, n = len(array1), len(array2)
    aux_array = [None] * (m + n)
    p1 = 0
    p2 = 0
    c = 0
    while p1 < m and p2 < n:
        if array1[p1] < array2[p2]:
            aux_array[c] = array1[p1]
            p1 += 1
        else:
            aux_array[c] = array2[p2]
            p2 += 1
        c += 1
    if p1 == m:  # array1 exhausted
        while p2 < n:
            aux_array[c] = array2[p2]
            p2 += 1
            c += 1
    elif p2 == n:  # array2 exhausted
        while p1 < m:
            aux_array[c] = array1[p1]
            p1 += 1
            c += 1
    return aux_array


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # array = [6, 5, 4, 3, 2, 1]
    # run_sorting_algorithm(algorithm="sorted", array=array)
    # run_sorting_algorithm(algorithm="bubble_sort", array=array)
    # run_sorting_algorithm(algorithm="selection_sort", array=array)
    # array = [
    #     2,
    #     3,
    #     5,
    #     7,
    #     11,
    #     13,
    #     17,
    #     19,
    #     23,
    #     29,
    #     31,
    #     37,
    #     41,
    #     43,
    #     47,
    #     53,
    #     59,
    #     61,
    #     67,
    #     71,
    #     73,
    #     79,
    #     83,
    #     89,
    #     97,
    # ]
    # shuffle(array)
    # print(array)
    # print(mergesort_recursive(array.copy()))
    # print(mergesort_iterative(array.copy()))
    # array = list(range(ARRAY_LENGTH))
    print(mergesort_iterative(array.copy()) == mergesort_recursive(array.copy()))
    run_sorting_algorithm(algorithm="mergesort_recursive", array=array.copy())
    run_sorting_algorithm(algorithm="mergesort_iterative", array=array.copy())
    run_sorting_algorithm(algorithm="quicksort_recursive", array=array.copy())
