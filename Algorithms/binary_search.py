def iterative_binary_search(nums, target):
    # TC - O(log(n))
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        if nums[lo] == target:
            return lo

        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid

    return -1


def recursive_binary_search(nums, target, lo, hi):
    # TC - O(log(n))
    if lo > hi:
        return -1

    if nums[lo] == target:
        return lo

    mid = (lo + hi) // 2
    if target < nums[mid]:
        return recursive_binary_search(nums, target, lo, mid - 1)
    elif target > nums[mid]:
        return recursive_binary_search(nums, target, mid + 1, hi)
    else:
        return mid


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    lo = 0
    hi = len(nums) - 1
    print(iterative_binary_search(nums, target=9))
    print(iterative_binary_search(nums, target=12))
    print(iterative_binary_search(nums, target=-1))
    print(iterative_binary_search(nums, target=999))
    print(recursive_binary_search(nums, target=9, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=12, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=-1, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=999, lo=lo, hi=hi))
    print()

    nums = [-1, 0, 3, 9, 12]
    lo = 0
    hi = len(nums) - 1
    print(iterative_binary_search(nums, target=9))
    print(iterative_binary_search(nums, target=12))
    print(iterative_binary_search(nums, target=-1))
    print(iterative_binary_search(nums, target=999))
    print(recursive_binary_search(nums, target=9, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=12, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=-1, lo=lo, hi=hi))
    print(recursive_binary_search(nums, target=999, lo=lo, hi=hi))
    print()

    nums = []
    lo = 0
    hi = len(nums) - 1
    print(iterative_binary_search(nums, target=999))
    print(recursive_binary_search(nums, target=999, lo=lo, hi=hi))
