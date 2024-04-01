def solve(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    ex = ''+str(sum)
    if (len(ex) == 1):
        return '0' + ex
    return ex


so = [1, 2, 3]
print(solve(so))
