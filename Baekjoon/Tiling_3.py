# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

# 입력: 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
# 출력: 첫째 줄에 경우의 수를 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
dp = dict()     # dp[k]: N= 2k일 때, 가로 길이가 2k인 타일들이 가질 수 있는 경우의 수

if N % 2 != 0:
    print(0)
else:
    k = int(N * 0.5)
    dp[0] = 1   # 경우의 수 구할 떄 0이 곱해지는 것 방지
    dp[1] = 3

    for i in range(2, k + 1):
        dp[i] = dp[i - 1] * 3   # 가로2 블록이 추가되는 3가지 경우
        for j in range(2, i + 1):
            dp[i] += (dp[i - j] * 2)    # 2개씩 추가되는 특수 케이스

    print(dp[k])
