# 민호와 강호가 2차원 좌표 평면 위에 있다.
# 민호는 점 A(Ax, Ay)에서 점 B(Bx, By)를 향해 걸어가고 있고, 강호는 점 C(Cx, Cy)에서 점 D(Dx, Dy)를 향해 걸어가고 있다.
# 민호와 강호는 동시에 출발하고, 민호가 점 B에 도착하는 순간 강호도 점 D에 도착한다. 또, 두 사람은 항상 일정한 속도로 걸어간다.
# 두 사람의 거리가 가장 가까울 때, 거리를 구하는 프로그램을 작성하시오.
#
# 두 점 (x1, y1), (x2, y2)사이의 거리는 ((x2-x1)^2 + (y2-y1)^2)^0.5 이다.
#
# 입력
# 첫째 줄에 Ax, Ay, Bx, By, Cx, Cy, Dx, Dy가 주어진다.
# 입력으로 주어지는 모든 좌표는 0보다 크거나 같고, 10000보다 작거나 같은 정수이다.
#
# 출력
# 민호와 강호가 가장 가까웠을 때의 거리를 출력한다.
# 절대/상대 오차는 10^-6까지 허용한다.

import sys


Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())


def get_squared_diff(x1, x2):
    return (x2 - x1) ** 2


start, end = 0, 100    # (relative time, 0~100%)
answer = sys.maxsize
while end - start > 10 ** -6:
    left = start + (end - start) * (1 / 3)
    right = start + (end - start) * (2 / 3)

    dist_x_at_left_1 = Ax + (Bx - Ax) * (left / 100)
    dist_x_at_left_2 = Cx + (Dx - Cx) * (left / 100)
    dist_y_at_left_1 = Ay + (By - Ay) * (left / 100)
    dist_y_at_left_2 = Cy + (Dy - Cy) * (left / 100)
    
    dist_x_at_left = get_squared_diff(dist_x_at_left_1, dist_x_at_left_2) + get_squared_diff(dist_y_at_left_1, dist_y_at_left_2)

    dist_x_at_right_1 = Ax + (Bx - Ax) * (right / 100)
    dist_x_at_right_2 = Cx + (Dx - Cx) * (right / 100)
    dist_y_at_right_1 = Ay + (By - Ay) * (right / 100)
    dist_y_at_right_2 = Cy + (Dy - Cy) * (right / 100)

    dist_x_at_right = get_squared_diff(dist_x_at_right_1, dist_x_at_right_2) + get_squared_diff(dist_y_at_right_1, dist_y_at_right_2)

    if dist_x_at_left <= dist_x_at_right:
        answer = min(answer, dist_x_at_left)
        end = right
    else:
        answer = min(answer, dist_x_at_right)
        start = left

print("%.10f" % (answer ** 0.5))
