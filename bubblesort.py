def bubblesort(array):
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
