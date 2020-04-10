# https://www.acmicpc.net/problem/2667
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
from collections import deque
import sys


N = int(sys.stdin.readline().rstrip())

# 상대 좌표
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 집을 표시 (1 or 0)
# (이후 dfs에서 방문한 집은 0으로 지워버려서 별도의 visited 리스트를 쓰지 않음)
H = []

for n in range(N):
    H.append([int(c) for c in sys.stdin.readline().rstrip()])

# print(*H, sep="\n")


def dfs(y, x):
    stack = deque()
    stack.append((y, x))
    ret = 1

    while len(stack) != 0:
        next_coord = None
        H[stack[-1][0]][stack[-1][1]] = 0

        for k in range(4):
            ny = dy[k] + stack[-1][0]
            nx = dx[k] + stack[-1][1]

            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue

            if H[ny][nx] == 0:
                continue

            next_coord = (ny, nx)
            stack.append((ny, nx))
            ret += 1
            break

        if next_coord is None:
            if len(stack) != 0:
                stack.pop()

    return ret


houses = []

for i in range(0, N):
    for j in range(0, N):
        if H[i][j] == 0:
            continue

        houses.append(dfs(i, j))


print(len(houses))
print(*sorted(houses), sep="\n")
