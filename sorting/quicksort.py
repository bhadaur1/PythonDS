from random import randint, shuffle


def quicksort_recursive(arr):
    """
    1. Pick a random element arr[pivotindx] as pivot
    2. Construct three arrays
        (a) less: all values < arr[pivotindx]
        (b) same: all values = arr[pivotindx]
        (c) more: all values > arr[pivotindx]
    3. recursively apply function to less and more
    """
    if len(arr) < 2:
        return arr

    pivotindx = randint(0, len(arr) - 1)

    less = []
    same = []
    more = []
    for val in arr:
        if val < arr[pivotindx]:
            less.append(val)
        elif val > arr[pivotindx]:
            more.append(val)
        else:
            same.append(val)
    return quicksort_recursive(less) + same + quicksort_recursive(more)


def quicksort_inplace(arr):
    """
    1. Randomly shuffle array to not get stuck with O(n^2) performance
    2. Apply recursive helper function to sort in place
    """
    shuffle(arr)
    __quicksortHelper__(arr, 0, len(arr) - 1)
    return arr


def __quicksortHelper__(arr, lo, hi):
    """
    Recursive helper for quicksorting
    """
    if lo >= hi:
        return
    pivotindx = __partition2way__(arr, lo, hi)
    __quicksortHelper__(arr, lo, pivotindx - 1)
    __quicksortHelper__(arr, pivotindx + 1, hi)


def __partition2way__(arr, lo, hi):
    """
    Function to achieve 2-way partitioning for quicksort
    Start with 2 pointers i and j, choose first element as pivot
    In each iteration, do the following in order:
        (a) Increment i until arr[i] >= arr[lo]
        (b) Decrement j until arr[j] <= arr[lo]
        (c) Check if pointers have crossed (j<=i), 
                if yes then swap arr[lo] with arr[j] and break out
        (d) If pointers didn't cross, then swap arr[i] with arr[j]
    Return the index of the pivot (j) so that it can be used by __quicksortHelper__
    """

    if len(arr) < 2:
        return arr

    # Define i and j pointers
    i = lo
    j = hi + 1

    while True:
        while i < hi:
            i += 1
            if arr[i] >= arr[lo]:
                # print("Break i at ", i)
                break

        while j > lo:
            j -= 1
            if arr[j] < arr[lo]:
                # print("Break j at ", j)
                break

        if j <= i:
            arr[lo], arr[j] = arr[j], arr[lo]
            break

        if arr[i] > arr[j]:
            # print(f"swap {arr[i]} with {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
        # print(arr)

    return j
