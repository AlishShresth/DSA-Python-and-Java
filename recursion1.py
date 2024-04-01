def printRecur(arr, size):
    if size == 1:
        return True
    if arr[size-2] < arr[size-1]:
        return printRecur(arr, size-1)
    return False


def firstOccur(arr, i, key):
    if i == len(arr):
        return -1
    if arr[i] == key:
        return i
    return firstOccur(arr, i+1, key)


def lastOccur(arr, size, key):
    if size == 0:
        return -1
    if arr[size-1] == key:
        return size-1
    return lastOccur(arr, size-1, key)


def powerN(base, exp):
    if (exp == 0):
        return 1
    halfPower = powerN(base, exp//2)
    halfPowerSq = halfPower * halfPower
    if (exp % 2 != 0):
        halfPowerSq *= base
    return halfPowerSq


arr = [5, 6, 8, 10, 10, 10, 6]
print(powerN(2, 10))
