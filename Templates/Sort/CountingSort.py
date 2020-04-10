

# arr: 정렬할 배열, 리스트
# k: arr 의 최대값
def counting_sort(arr, k):
    ret = [-1] * len(arr)

    # 카운트 초기화
    count = [0] * (k + 1)

    for a in arr:
        count[a] += 1

    for i in range(k):
        count[i + 1] += count[i]

    for j in range(len(arr)):
        ret[count[arr[j]] - 1] = arr[j]
        count[arr[j]] -= 1

    return ret


print(counting_sort([1, 23, 3, 43], 43))
