import sys
arr = [5, 2, 1, 4, 3]
for i in range(len(arr)-1):
    posmin = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[posmin]:
            posmin = j
    temp = arr[posmin]
    arr[posmin] = arr[i]
    arr[i] = temp
print(arr)
