# https://www.acmicpc.net/problem/1003
#
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 출력: 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
import sys


memo = [None]*40


def fibonacci_cnt(n):
    if n == 0:
        memo[0] = [1, 0]
        return memo[0]
    elif n == 1:
        memo[1] = [0, 1]
        return memo[1]
    else:
        if memo[n - 1] is not None:
            fib_n_1 = memo[n - 1]
        else:
            memo[n - 1] = fibonacci_cnt(n - 1)
            fib_n_1 = memo[n - 1]
        if memo[n - 2] is not None:
            fib_n_2 = memo[n - 2]
        else:
            memo[n - 2] = fibonacci_cnt(n - 2)
            fib_n_2 = memo[n - 2]

        return [sum(x) for x in zip(fib_n_1, fib_n_2)]


N = int(sys.stdin.readline())
ans = [[0, 0]]*N

for i in range(0, N):
    ans[i] = fibonacci_cnt(int(sys.stdin.readline()))
    print(*ans[i])
