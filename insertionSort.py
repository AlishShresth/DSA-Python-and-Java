arr = [6, 1, 2, 5, 5, 4, 5, 6, 2]
for i in range(1, len(arr)):
    temp = arr[i]
    prev = i-1
    while (prev >= 0 and arr[prev] > temp):
        arr[prev+1] = arr[prev]
        prev -= 1
    arr[prev+1] = temp

print(arr)
