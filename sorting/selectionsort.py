def selectionsort(arr):
    """
    In each iteration, find the min of arr[lo:hi+1]
    and swap with arr[lo], then increment lo
    Invariant: everything to the left of lo is sorted
    """
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        minval = arr[lo]
        minindx = lo
        for curr in range(lo + 1, hi + 1):
            if arr[curr] < minval:
                minval = arr[curr]
                minindx = curr
        arr[lo], arr[minindx] = arr[minindx], arr[lo]
        # print(arr)
        lo += 1
    return arr
