# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
from collections import deque
import sys


N = int(sys.stdin.readline().rstrip())
edge_connected = [[]for i in range(N + 1)]
parent = [0] * (N + 1)
for n in range(1, N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edge_connected[a].append(b)
    edge_connected[b].append(a)


def bfs(edge_info):
    queue = deque()
    parent[1] = 1
    queue.append(1)

    while len(queue) != 0:
        p = queue.popleft()

        for c in edge_info[p]:
            if parent[c] > 0:
                continue
            parent[c] = p
            queue.append(c)


bfs(edge_connected)
for p in range(2, N + 1):
    print(parent[p])
