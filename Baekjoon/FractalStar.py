# https://www.acmicpc.net/problem/2447

# 입력: 첫째 줄에 N이 주어진다.
# N은 항상 3의 제곱꼴인 수이다. (3, 9, 27, ...)
# (N=3^k, 1 ≤ k < 8)

# 출력: 첫째 줄부터 N번째 줄까지 별을 출력한다.
import math
import sys


def draw_star(ret, power, first_point_row, first_point_col):
    if power == 1:
        ret[first_point_row + 1][first_point_col + 1] = " "
        return ret

    new_power = power - 1
    unit_dist = 3 ** new_power
    unit_dist_doubled = 2 * unit_dist

    ret = draw_star(ret, new_power, first_point_row, first_point_col)
    ret = draw_star(ret, new_power, first_point_row, first_point_col + unit_dist)
    ret = draw_star(ret, new_power, first_point_row, first_point_col + unit_dist_doubled)

    ret = draw_star(ret, new_power, first_point_row + unit_dist, first_point_col)
    # draw empty
    for row in range(first_point_row + unit_dist, first_point_row + unit_dist_doubled):
        for col in range(first_point_col + unit_dist, first_point_col + unit_dist_doubled):
            ret[row][col] = " "
    ret = draw_star(ret, new_power, first_point_row + unit_dist, first_point_col + unit_dist_doubled)

    ret = draw_star(ret, new_power, first_point_row + unit_dist_doubled, first_point_col)
    ret = draw_star(ret, new_power, first_point_row + unit_dist_doubled, first_point_col + unit_dist)
    ret = draw_star(ret, new_power, first_point_row + unit_dist_doubled, first_point_col + unit_dist_doubled)

    return ret


N = int(sys.stdin.readline().rstrip())
target_power = round(math.log(N, 3))
stars = [["*" for col in range(N)] for row in range(N)]
stars = draw_star(stars, target_power, 0, 0)

for row in stars:
    print(*row, sep="")

# 느려서 실패한 문제.