def mergesort_recursive(arr):
    """
    Recursively divide and merge sorted subarrays
    """
    if len(arr) == 1:
        return arr
    lo = 0
    hi = len(arr) - 1
    mid = (lo + hi) // 2

    arr1 = mergesort_recursive(arr[: mid + 1])
    arr2 = mergesort_recursive(arr[mid + 1 :])

    return __merge2sorted__(arr1, arr2)


def mergesort_iterative(arr):
    """
    Start with merging adjacent subarrays of size 1
    In each iteration, double the size of subarrays.
    """
    s = 1
    while s < len(arr):
        # print(f"Merging sorted subarrays of size {s}")
        i = 0
        while i < len(arr):
            # print(f"merge {arr[i:i+s]} and {arr[i+s:i+2*s]}")
            arr[i : i + 2 * s] = __merge2sorted__(
                arr[i : i + s], arr[i + s : i + 2 * s]
            )
            i = i + 2 * s
        # print(arr)
        s = s * 2
    return arr


def __merge2sorted__(arr1, arr2):
    """
    Takes two sorted subarrays and returns a sorted array
    """
    m, n = len(arr1), len(arr2)
    aux_arr = [None] * (m + n)
    p1 = 0
    p2 = 0
    c = 0
    while p1 < m and p2 < n:
        if arr1[p1] < arr2[p2]:
            aux_arr[c] = arr1[p1]
            p1 += 1
        else:
            aux_arr[c] = arr2[p2]
            p2 += 1
        c += 1
    if p1 == m:  # arr1 exhausted
        while p2 < n:
            aux_arr[c] = arr2[p2]
            p2 += 1
            c += 1
    elif p2 == n:  # arr2 exhausted
        while p1 < m:
            aux_arr[c] = arr1[p1]
            p1 += 1
            c += 1
    return aux_arr
