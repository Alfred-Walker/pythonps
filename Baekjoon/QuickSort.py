def partition(left_index, right_index, list_to_sort):
    if left_index >= right_index:
        return

    pivot_index = left_index
    j = pivot_index
    for i in range(left_index + 1, right_index + 1):
        if list_to_sort[i] < list_to_sort[pivot_index]:
            j += 1
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    new_pivot_index = j     # 복습시 가독성을 위해 임시 변수 설정
    list_to_sort[pivot_index], list_to_sort[new_pivot_index] = list_to_sort[new_pivot_index], list_to_sort[pivot_index]

    return new_pivot_index


def quick_coord_sort(left_index, right_index, list_to_sort):
    if left_index >= right_index:
        return

    pivot_index = partition(left_index, right_index, list_to_sort)
    #print(pivot_index)
    quick_coord_sort(left_index, pivot_index - 1, list_to_sort)
    quick_coord_sort(pivot_index + 1, right_index, list_to_sort)


example = [33, 12, 14, 2, 3]
quick_coord_sort(0, len(example) - 1, example)
print(example)