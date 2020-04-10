import sys


def merge_sort(_nums):
    if len(_nums) is 1:
        return _nums

    mid = len(_nums)//2
    left = _nums[:mid]
    right = _nums[mid:]
    left_len = len(left)
    right_len = len(right)

    left = merge_sort(left)
    right = merge_sort(right)

    li = 0
    ri = 0

    merged = []

    while left_len > li and right_len > ri:
        if left[li] <= right[ri]:
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1

    if left_len > li:
        merged += left[li:]
    elif right_len > ri:
        merged += right[ri:]

    return merged


N = int(sys.stdin.readline().rstrip())
nums = [0]*N

for i in range(0, N):
    nums[i] = int(sys.stdin.readline().rstrip())

nums = merge_sort(nums)
for i in nums:
    print(i)
