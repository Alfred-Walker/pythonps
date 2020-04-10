# https://www.acmicpc.net/problem/10451

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.
#
# 출력
# 각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
# 4: 40
from collections import deque
import sys
sys.setrecursionlimit(10**6)


T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N = int(sys.stdin.readline().rstrip())
    P = list(map(int, sys.stdin.readline().rstrip().split()))
    adjacent = [[] for i in range(N + 1)]
    for i in range(1, N + 1):
        adjacent[i].append(P[i - 1])

    visited = [False] * (N + 1)

    def dfs(start):
        stack = deque()
        visited[start] = True
        stack.append(start)

        while len(stack) != 0:
            for adv in adjacent[stack[-1]]:
                if not visited[adv]:
                    dfs(adv)

            if len(stack) != 0:
                stack.pop()

    cnt_permutation_cycle = 0
    for n in range(1, N + 1):
        if not visited[n]:
            dfs(n)
            cnt_permutation_cycle += 1

    print(cnt_permutation_cycle)
