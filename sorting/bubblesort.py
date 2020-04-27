def bubblesort(arr):
    n = len(arr)
    # print(arr)
    for i in range(n):
        already_sorted = True
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                already_sorted = False
                # print(arr)
        if already_sorted:
            break

    return arr
