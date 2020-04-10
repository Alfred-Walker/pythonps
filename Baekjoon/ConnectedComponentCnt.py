# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
#
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v)
#
# 같은 간선은 한 번만 주어진다.
#
# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

from collections import deque
import sys


adjacent_dict = dict()
visited = [False] * 1001
N, M = map(int, sys.stdin.readline().rstrip().split())

# 서로 연결되지 않은 1개의 고립된 정점도 셀 수 잇도록 한다.
for i in range(1, N + 1):
    adjacent_dict[i] = []

for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    adjacent_dict[u].append(v)
    adjacent_dict[v].append(u)

answer = 0
stack = deque()

for key in adjacent_dict.keys():
    if visited[key]:
        continue

    answer += 1
    stack.clear()
    stack.append(key)

    while len(stack) != 0:
        if not visited[stack[-1]]:
            visited[stack[-1]] = True

        to_visit = None

        for adv in adjacent_dict[stack[-1]]:
            if visited[adv]:
                continue

            to_visit = adv
            break

        if to_visit is not None:
            stack.append(to_visit)
        else:
            stack.pop()


print(answer)
