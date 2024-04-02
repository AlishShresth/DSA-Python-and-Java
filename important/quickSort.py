arr = [5, 1, 4, 6, 3, 7, 2]


def quickSort(arr, lo, hi):
    if lo >= hi:
        return
    pivotIDx = partition(arr, lo, hi)
    quickSort(arr, lo, pivotIDx-1)
    quickSort(arr, pivotIDx+1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo-1
    for j in range(lo, hi):
        if (arr[j] <= pivot):
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    i += 1
    temp = pivot
    arr[hi] = arr[i]
    arr[i] = temp
    return i


quickSort(arr, 0, len(arr)-1)
print(arr)
