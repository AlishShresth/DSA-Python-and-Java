def containsDuplicate(arr: list) -> bool:
    hashmap = set()
    for i in range(len(arr)):
        if arr[i] in hashmap:
            return True
        else:
            hashmap.add(arr[i])
    return False


print(containsDuplicate([1, 2, 3, 4, 1]))
