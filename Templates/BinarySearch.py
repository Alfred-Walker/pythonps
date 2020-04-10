def BinarySearch(num_list, target):
    num_list.sort()

    start = 0
    end = len(num_list) - 1
    mid = (start + end) // 2

    while start <= end:
        if num_list[mid] == target:
            return mid

        if num_list[mid] < target:
            start = mid + 1
            continue

        if num_list[mid] > target:
            end = mid - 1

    return -1
