# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

import sys


N = int(sys.stdin.readline().rstrip())

print(" " * (N - 1) + "*")

for i in range(2, N):
    left = " " * (N - i) + "*"
    right = " " * (2 * (i - 1) - 1) + "*"
    print(left + right)

if N != 1:
    print("*" * (2 * N - 1))
