from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().rstrip())
island_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

visited = [[False for i in range(N)] for j in range(N)]
answer = sys.maxsize
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def give_index_by_dfs(y, x, num):
    visited[y][x] = True
    island_map[y][x] = num  # 첫칸은 직접 바꾸는 것에 주의

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if visited[ny][nx] or island_map[ny][nx] == 0:
            continue

        give_index_by_dfs(ny, nx, num)


def get_bridge_length(idx):
    queue = deque()
    bridge_length = 0
    for y in range(N):
        for x in range(N):
            if island_map[y][x] == idx:
                visited[y][x] = True
                queue.append((y, x))

    while len(queue) != 0:
        queue_size = len(queue)
        for i in range(queue_size):
            y, x = queue.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue

                if visited[ny][nx]:
                    continue

                if island_map[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                else:
                    # print("idx: {0}, island_map[{1}][{2}]: {3}".format(idx, ny, nx, island_map[ny][nx]))
                    return bridge_length

        bridge_length += 1

    return sys.maxsize


index = 1
for j in range(N):
    for i in range(N):
        if visited[j][i]:
            continue

        if island_map[j][i] == 0:
            continue

        give_index_by_dfs(j, i, index)
        index += 1


for idx in range(1, index + 1):
    visited = [[False for i in range(N)] for j in range(N)]
    answer = min(answer, get_bridge_length(idx))

print(answer)
