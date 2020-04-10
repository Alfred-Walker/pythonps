# https://www.acmicpc.net/problem/9461
# 1:40
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

# 출력
# 각 테스트 케이스마다 P(N)을 출력한다.
import sys


T = int(sys.stdin.readline().rstrip())
N = [int(sys.stdin.readline().rstrip()) for n in range(T)]

dp = dict()
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2


def get_padovan(num):
    for i in range(6, num + 1):
        dp[i] = dp[i - 5] + dp[i - 1]

    return dp[num]


for n in N:
    print(get_padovan(n))
