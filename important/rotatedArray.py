def findIndex(target: int, nums: list) -> int:
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            return mid
        elif nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[hi] >= target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


nums = [0, 1, 2, 3, 5, 6]
print(findIndex(7, nums))
