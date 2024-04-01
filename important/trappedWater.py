def trap(arr):
    size = len(arr)
    leftMaxBound = []
    leftMaxBound.append(arr[0])
    for i in range(1, size):
        leftMaxBound.append(max(arr[i], leftMaxBound[i-1]))
    rightMaxBound = [None] * size
    rightMaxBound[size-1] = arr[size-1]
    for i in range(size-2, -1, -1):
        rightMaxBound[i] = max(rightMaxBound[i+1], arr[i])
    trappedWater = 0
    for i in range(size):
        waterLevel = min(leftMaxBound[i], rightMaxBound[i])
        trappedWater += waterLevel - arr[i]
    return trappedWater


print(trap([4, 2, 0, 3, 2, 5]))
