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
    lt, gt = __partition3way__(arr, lo, hi)
    __quicksortHelper__(arr, lo, lt - 1)
    __quicksortHelper__(arr, gt + 1, hi)


def __partition2way__(arr, lo, hi):
    """
    Function to achieve 2-way partitioning for quicksort
    1. Start with 2 pointers lt and gt, choose first element (lo) as pivot
    2. Invariant: everything to the left of lt is less than pivot, right of gt is larger than pivot
    3. In each iteration, do the following in order:
        (a) Increment lt until arr[lt] >= arr[lo]
        (b) Decrement gt until arr[gt] <= arr[lo]
        (c) Check if pointers have crossed (gt<=lt), 
                if yes then swap arr[lo] with arr[gt] and break out
        (d) If pointers didn't cross, then swap arr[lt] with arr[gt]
    4. Return the index of the pivot (now gt) so that it can be used by __quicksortHelper__
    """

    if lo >= hi:
        return

    # Define lt and gt pointers
    lt = lo
    gt = hi + 1

    while True:
        while lt < hi:
            lt += 1
            if arr[lt] >= arr[lo]:
                # print("Break lt at ", lt)
                break

        while gt > lo:
            gt -= 1
            if arr[gt] < arr[lo]:
                # print("Break gt at ", gt)
                break

        if gt <= lt:
            arr[lo], arr[gt] = arr[gt], arr[lo]
            break

        if arr[lt] > arr[gt]:
            # print(f"swap {arr[lt]} with {arr[gt]}")
            arr[lt], arr[gt] = arr[gt], arr[lt]
        # print(arr)

    return gt


def __partition3way__(arr, lo, hi):
    """
    Function to achieve 3-way partitioning for quicksort
    1. Start with 3 pointers (lt, i, gt), choose first element (lo) as pivot
    2. Invariant: everything to the
        (a) left of lt is less than pivot
        (b) between lt and i is equal to pivot
        (c) right of gt is larger than pivot
    3. In each iteration, while i<gt do from left to right :
        (a) if arr[i] < arr[lo] exchange arr[lt] and arr[i], increment lt and i
        (b) if arr[i] == arr[lo] increment only i
        (b) if arr[i] > arr[lo] exchange arr[gt] and arr[i], decrement gt 
    4. Return lt, gt
    """

    if hi <= lo:
        return lo, hi

    # Define lt and gt pointers
    lt = lo
    i = lt + 1
    gt = hi
    v = arr[lo]

    while i <= gt:
        if arr[i] < v:
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        elif arr[i] > v:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt
