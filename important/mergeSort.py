arr = [5, 3, 1, 2, 6, 4, 8]


def mergeSort(arr, lo, hi):
    if (lo >= hi):
        return
    mid = lo + (hi-lo)//2
    mergeSort(arr, lo, mid)
    mergeSort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)


def merge(arr, lo, mid, hi):
    tempArr = []
    i = lo
    j = mid+1
    k = 0
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tempArr.append(arr[i])
            i += 1
        else:
            tempArr.append(arr[j])
            j += 1
    while i <= mid:
        tempArr.append(arr[i])
        i += 1
    while j <= hi:
        tempArr.append(arr[j])
        j += 1
    i = lo
    for k in range(len(tempArr)):
        arr[i] = tempArr[k]
        i += 1


mergeSort(arr, 0, len(arr)-1)
print(arr)
