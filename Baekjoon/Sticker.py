# https://www.acmicpc.net/problem/9465
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다.
# 다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다.
# 연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.

import sys


T = int(sys.stdin.readline().rstrip())
sticker = [dict() for t in range(T)]

for t in range(1, T + 1):
    N = int(sys.stdin.readline().rstrip())
    dp = dict()
    dp[1] = [0 for n in range(N + 1)]
    dp[2] = [0 for n in range(N + 1)]
    sticker = dict()
    sticker[1] = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    sticker[2] = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

    # dp[i][j]: i행 j열의 스티커를 떼었을 때 가질 수 있는 점수의 최댓값
    # (두 칸을 건너뛰면 한 칸씩 대각선 건너는 것과 같은 지점을 가지만 점수는 건너뛰므로 항상 손해를 본다)
    # dp[1][j] = max(dp[2][j-1], dp[2][j-2]) + sticker[1][j]
    # dp[2][j] = max(dp[1][j-1], dp[1][j-2]) + sticker[2][j]

    # base case
    dp[1][1] = sticker[1][1]
    dp[2][1] = sticker[2][1]

    for j in range(2, N + 1):
        dp[1][j] = max(dp[2][j - 1], dp[2][j - 2]) + sticker[1][j]
        dp[2][j] = max(dp[1][j - 1], dp[1][j - 2]) + sticker[2][j]

    print(max(dp[1][N], dp[2][N]))
