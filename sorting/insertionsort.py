def insertionsort(arr):
    """
    In a given iteration:
        1. swap arr[lo] with each larger entry to the left.
        2. Increment lo pointer
    """
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        curr = lo
        while curr - 1 >= 0:
            if arr[curr] < arr[curr - 1]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
            curr -= 1
        lo += 1
    return arr
