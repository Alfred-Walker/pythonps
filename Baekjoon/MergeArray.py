# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
#
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.
#
# 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

merged = [None] * (N + M)
i, j = 0, 0

for k in range(N + M):
    if i >= N:
        merged[k] = B[j]
        j += 1
        continue

    if j >= M:
        merged[k] = A[i]
        i += 1
        continue

    if A[i] <= B[j]:
        merged[k] = A[i]
        i += 1
    else:
        merged[k] = B[j]
        j += 1

print(*merged)
