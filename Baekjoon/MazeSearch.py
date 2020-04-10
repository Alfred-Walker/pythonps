# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	 0	1	1	1	1
# 1	 0	1	0	1	0
# 1	 0	1	0	1	1
# 1	 1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
#
# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

from collections import deque
import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = []
for n in range(N):
    maze.append([int(c) for c in sys.stdin.readline().rstrip()])

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

visited = [[0 for m in range(M)] for n in range(N)]


# bfs(y, x): 시작 지점으로부터 목표 지점까지의 경로를 찾아 거리를 리턴
def bfs(target_y, target_x):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while len(queue) != 0:
        q = queue.popleft()
        y, x = q

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if visited[ny][nx] > 0 or maze[ny][nx] == 0:
                continue

            visited[ny][nx] = visited[y][x] + 1
            if ny == target_y and nx == target_x:
                return visited[ny][nx]
            else:
                queue.append((ny, nx))

    return visited[target_y][target_x]


print(bfs(N - 1, M - 1))
