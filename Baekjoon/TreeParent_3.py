import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().rstrip())
edge_connected = [[]for i in range(N + 1)]
parent = [0] * (N + 1)
for n in range(1, N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edge_connected[a].append(b)
    edge_connected[b].append(a)


def dfs(pi):
    for ci in edge_connected[pi]:
        if parent[ci] > 0:
            continue
        parent[ci] = pi
        dfs(ci)


parent[1] = 1
dfs(1)
for p in range(2, N + 1):
    print(parent[p])
