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
from queue import LifoQueue
from queue import Queue
import sys


N, M, V = map(int, sys.stdin.readline().rstrip().split())
adjacent_list = [[] for _ in range(N + 1)]
adjacent_matrix = [[0]*(N + 1) for _ in range(N + 1)]
checked_DFS = [False] * (N + 1)
checked_BFS = [False] * (N + 1)
answer_DFS = [] * N
answer_BFS = [] * N
for n in range(0, M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adjacent_matrix[a][b] = True
    adjacent_matrix[b][a] = True

    if a not in adjacent_list[b]:
        adjacent_list[b].append(a)

    if b not in adjacent_list[a]:
        adjacent_list[a].append(b)

for a in adjacent_list:
    a.sort()

# print(*adjacent_list, end="\n")
# print(*adjacent_matrix, sep="\n")

# DFS
stack = LifoQueue()
stack.put(V)
while not stack.empty():
    v_to_check = stack.get()    # pop temporarily instead of peek
    if not checked_DFS[v_to_check]:
        checked_DFS[v_to_check] = True
        answer_DFS.append(v_to_check)
    no_way_to_go = True

    for a in adjacent_list[v_to_check]:  # check whether the a is adjacent to v_to_check
        if not checked_DFS[a]:
            stack.put(v_to_check)
            stack.put(a)
            no_way_to_go = False
            break

# BFS
queue = Queue()
queue.put(V)
checked_BFS[V] = True
answer_BFS.append(V)
while not queue.empty():
    v_to_check = queue.get()   # pop temporarily instead of peek

    for a in adjacent_list[v_to_check]: # check whether the a is adjacent to v_to_check
        if not checked_BFS[a]:
            queue.put(a)
            checked_BFS[a] = True
            answer_BFS.append(a)


print(*answer_DFS)
print(*answer_BFS)
