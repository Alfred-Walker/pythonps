# 문제
# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다.
# 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.
#
# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다.
# 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다.
# 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다.
# 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.
#
# 입력
# 첫째 줄에 N(1≤N≤500,000)이 주어진다.
# 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다.
# 각각의 A[i]는 0≤|A[i]|≤1,000,000,000의 범위에 들어있다.
#
# 출력
# 첫째 줄에 Swap 횟수를 출력한다

import sys


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_sorted = [0] * N
swap_cnt = 0


def merge(list_to_sort, sorted_list, left, right, mid):
    global swap_cnt
    i = left
    j = mid + 1
    k = left

    # 좌, 우측 중 어느 한쪽이 먼저 정렬될 때까지 루프
    while i <= mid and j <= right:
        if list_to_sort[i] <= list_to_sort[j]:
            sorted_list[k] = list_to_sort[i]
            i += 1
            k += 1
        else:
            sorted_list[k] = list_to_sort[j]
            swap_cnt += mid + 1 - i     # mid + 1 - left는 초기 왼쪽 리스트의 아이템 개수
            j += 1
            k += 1

    # whil문 이후 남은 항목 추가
    if i <= mid:
        while i <= mid:
            sorted_list[k] = list_to_sort[i]
            i += 1
            k += 1
    else:
        while j <= right:
            sorted_list[k] = list_to_sort[j]
            j += 1
            k += 1

    # sorted list를 list_to_sort에도 반영
    for k in range(left, right + 1):
        list_to_sort[k] = sorted_list[k]


def merge_sort(list_to_sort, sorted_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(list_to_sort, sorted_list, left, mid)
    merge_sort(list_to_sort, sorted_list, mid + 1, right)
    merge(list_to_sort, sorted_list, left, right, mid)


merge_sort(A, A_sorted, 0, N - 1)
print(swap_cnt)
