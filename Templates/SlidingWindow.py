from collections import deque

# 크기 n 인 수열으로 만들 수 있는 크기 k 의 부분 수열의 최대값 O(n*k)
def get_sliding_window_max(arr, n, k):
    current_max = 0

    for i in range(n - k + 1):
        current_max = arr[i]
        for j in range(1, k):
            current_max = max(current_max, arr[i+j])

        print(str(current_max) + " ", end="")


# 크기 n 인 수열으로 만들 수 있는 크기 k 의 부분 수열의 최소값 O(n*k)
def get_sliding_window_min(arr, n, k):
    current_min = 0

    for i in range(n - k + 1):
        current_min = arr[i]
        for j in range(1, k):
            current_min = min(current_min, arr[i+j])

        print(str(current_min) + " ", end="")


# 길이 n 인 수열으로 만들 수 있는 크기 k 의 부분 수열의 최대값 O(n*k)
def get_sliding_window_max2(arr, n, k):
    my_deque = deque()
    ret = []

    for i in range(n):
        to_check = (arr[i], i)      # (value, index) tuple 로 저장
        # print("{0} - {1}: {2}".format(i, k, i - k))
        # 지정 범위 밖인 deque 항목 삭제
        if len(my_deque) != 0 and my_deque[0][1] <= i - k:
            my_deque.popleft()

        while len(my_deque) != 0 and my_deque[-1][0] < to_check[0]:
            my_deque.pop()

        my_deque.append(to_check)

        if i - k >= -1:
            ret.append(my_deque[0][0])

    return ret


# 길이 n 인 수열으로 만들 수 있는 크기 k 의 부분 수열의 최소값 O(n*k)
def get_sliding_window_min2(arr, n, k):
    my_deque = deque()
    ret = []

    for i in range(n):
        to_check = (arr[i], i)  # (value, index) tuple 로 저장
        # print("{0} - {1}: {2}".format(i, k, i - k))
        # 지정 범위 밖인 deque 항목 삭제
        if len(my_deque) != 0 and my_deque[0][1] <= i - k:
            my_deque.popleft()

        while len(my_deque) != 0 and my_deque[-1][0] > to_check[0]:
            my_deque.pop()

        my_deque.append(to_check)

        if i - k >= -1:
            ret.append(my_deque[0][0])

    return ret



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = [12, 1, 78, 90, 57, 89, 56]
    n = len(arr)
    k = 3
    get_sliding_window_max(arr, n, k)
    print("\n")
    get_sliding_window_min(arr, n, k)
    print("\n")
    print(get_sliding_window_max2(arr, n, k))
    print("\n")
    print(get_sliding_window_min2(arr, n, k))
    print("\n")
