# https://www.acmicpc.net/problem/7576
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
# 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
#
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
#
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
#
# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
# 단, 2 ≤ M,N ≤ 1,000 이다.
#
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
#
# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
from collections import deque
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
TOMATO = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

day = 0


def bfs(tomato_box, width, height):
    queue = deque()

    # 이미 익어있는 토마토들의 주변을 검사할 것이므로
    # 익어있는 토마토들(1)을 모두 큐에 집어넣음
    for j in range(height):
        for i in range(width):
            if tomato_box[j][i] == 1:
                queue.append((j, i))

    while len(queue) != 0:
        t = queue.popleft()
        x = t[1]
        y = t[0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 밖 인덱스 제외
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            # 새로 익은 토마토에 대해 익은 토마토의 값 + 1을 할당 (day + 1 에 해당)
            if TOMATO[ny][nx] == 0:
                queue.append((ny, nx))
                TOMATO[ny][nx] = TOMATO[y][x] + 1


bfs(TOMATO, M, N)
day = 0

# bfs 이후 모든 토마토를 검사
for y in range(N):
    for x in range(M):
        # 만약 하나라도 익지 않은 토마토가 남아있다면 -1 출력 후 종료
        if TOMATO[y][x] == 0:
            print(-1)
            exit(0)

        day = max(day, TOMATO[y][x])


print(day - 1)  # 처음에 익은 토마토를 나타내는 TOMATO[y][x] == 1일 때, day는 0이었므로 1을 빼줌
