# 입력: 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수들의 범위는 int 로 한다.

# 출력: M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
from sys import stdin


def binary_search(start, end, num_to_find):
    while start <= end:
        mid = start + int(end - start) >> 1

        if num_set[mid] == num_to_find:
            return 1
        elif num_set[mid] > num_to_find:
            end = mid - 1
        elif num_set[mid] < num_to_find:
            start = mid + 1

    return 0


N = int(stdin.readline().rstrip())
num_set = list(map(int, stdin.readline().rstrip().split()))
num_set.sort()
M = int(stdin.readline().rstrip())
nums_to_find = list(map(int, stdin.readline().rstrip().split()))
for n in nums_to_find:
    print(binary_search(0, N - 1, n))
