def quicksort(start, end, array):
    end -= 1
    if (start < end):
        pIndex = partition(start, end, array)
        quicksort(start, pIndex - 1, array)
        quicksort(pIndex + 1, end, array)

    return array


def partition(start, end, array):
    pIndex = start
    pivot = array[end]

    for i in range(0, end):
        if array[i]<=pivot:
            array[i], array[pIndex] = array[pIndex], array[i]
            pIndex+=1

    array[end], array[pIndex] = array[pIndex], array[end]

    return pIndex