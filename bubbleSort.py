arr = [1, 2, 5, 5, 4, 5, 6, 2]
for i in range(len(arr) - 1):
    swaps = 0
    print('loop ran')
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swaps += 1
    if swaps == 0:
        break
print(arr)
