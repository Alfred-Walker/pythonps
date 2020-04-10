# https://codeforces.com/contest/1182/problem/0
import sys


N = int(sys.stdin.readline().rstrip())
dp = dict()
dp[1] = 0
dp[2] = 2
dp[3] = 0
# dp[4] = dp[2] * dp[2]
# dp[n] = dp[n-2] * dp[2]

if N % 2 == 1:
    print(0)
else:
    for n in range(4, N + 1, 2):
        dp[n] = dp[n-2] * dp[2]

    print(dp[N])
