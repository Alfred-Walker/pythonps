# 문제
# 알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다.
# 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
#
# 알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다.
# 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
# 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
# 단, 미로의 밖으로 이동 할 수는 없다.
#
# 벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다.
# 벽을 부수면, 빈 방과 동일한 방으로 변한다.
#
# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다.
# 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다.
# 0은 빈 방을 의미하고, 1은 벽을 의미한다.
#
# (1, 1)과 (N, M)은 항상 뚫려있다.
#
# 출력
# 첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.


import sys
sys.setrecursionlimit(10 ** 6)


M, N = map(int, sys.stdin.readline().rstrip().split())
maze = [sys.stdin.readline().rstrip() for i in range(N)]
visited = [[False] * M for i in range(N)]
crashed = [[sys.maxsize] * M for i in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0

# 시작점에서 출발하는 트리내의 위치들과
# 종점에서 출발하는 트리 내의 위치들 중 최단거리인 곳을 찾아 계산?
# => 잘못된 접근.
# 반례
# 000000
# 011001
# S0000G


# 시간, 메모리 초과?
def dfs(y, x, crash_cnt):
    if visited[y][x]:
        return

    if crashed[y][x] <= crash_cnt:
        return
    else:
        crashed[y][x] = crash_cnt

    if y == N - 1 and x == M - 1:
        return

    for i in range(0, 4):
        next_y = y + dy[i]
        next_x = x + dx[i]

        if 0 <= next_y < N:
            if 0 <= next_x < M:
                visited[y][x] = True
                if maze[next_y][next_x] == '0':
                    dfs(next_y, next_x, crash_cnt)
                else:
                    dfs(next_y, next_x, crash_cnt + 1)
                visited[y][x] = False


dfs(0, 0, 0)
print(crashed[N - 1][M - 1])
