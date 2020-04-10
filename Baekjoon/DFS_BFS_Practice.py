# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.

# 입력: 첫째 줄에
# 정점의 개수 N(1 ≤ N ≤ 1,000),
# 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다.

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.
from collections import deque
import sys

adjacent_dict = dict()
visited = [False] * 1001
answer_DFS = []
answer_BFS = []
N, M, V = map(int, sys.stdin.readline().rstrip().split())
for m in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a not in adjacent_dict.keys():
        adjacent_dict[a] = [b]
    else:
        adjacent_dict[a].append(b)

    if b not in adjacent_dict.keys():
        adjacent_dict[b] = [a]
    else:
        adjacent_dict[b].append(a)


for key in adjacent_dict:
    adjacent_dict[key].sort()

# DFS
stack = deque()
stack.append(V)
while len(stack) != 0:
    adv_to_visit = None
    top = stack[-1]

    if not visited[top]:
        answer_DFS.append(top)
        visited[top] = True

    if top in adjacent_dict.keys():
        for adv in adjacent_dict[top]:
            if visited[adv]:
                continue

            adv_to_visit = adv
            stack.append(adv_to_visit)
            break

    if adv_to_visit is None:
        stack.pop()

print(*answer_DFS)

# BFS
visited = [False] * 1001
queue = deque()
queue.append(V)

while len(queue) != 0:
    front = queue.popleft()

    if not visited[front]:
        visited[front] = True
        answer_BFS.append(front)

    if front in adjacent_dict.keys():
        for adv in adjacent_dict[front]:
            if visited[adv]:
                continue

            queue.append(adv)


print(*answer_BFS)
