# 벌집 문제
# https://www.acmicpc.net/problem/2292
# 입력: 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.
# 출력: 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
import math
import sys


def get_depth(_n):
    if _n is 1:
        return 1
    else:
        return math.ceil(math.sqrt((_n - 1)/3 + 0.25) + 0.5)


N = int(sys.stdin.readline().rstrip())
print(get_depth(N))
