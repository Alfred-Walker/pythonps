from collections import deque


def bfs(adj, visited, start):
    queue = deque()
    queue.append(start)

    while queue:
        u = queue.popleft()
        visited.append(u)

        for a in adj[u]:
            if a not in visited:
                queue.append(a)