from sys import stdin
import sys
sys.setrecursionlimit(10**6)


N, M = map(int, stdin.readline().rstrip().split())

num = list(range(1, N + 1))
visited = [False] * (N + 1)
selected = [0] * M

# dfs 와 visited 기록에 유의
def select(cnt):
    if cnt >= M:
        print(*selected)
        return

    for i in range(0, N):
        if not visited[i + 1]:
            visited[i + 1] = True       # 방문
            selected[cnt] = num[i]
            select(cnt + 1)
            visited[i + 1] = False      # 방문 취소


select(0)
