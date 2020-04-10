# 입력: 첫째 줄에 N이 주어진다. N은 항상 3×2^k 수이다. (3, 6, 12, 24, 48, ...) (k ≤ 10)
# 출력: 첫째 줄부터 N번째 줄까지 별을 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())

stars = ["" for i in range(0, N)]

for i in range(0, len(stars)):
    stars[i] += " " * (N - 1 - i)


def draw_triforce(_start_row, _row_count):
    if int(_row_count) == 3:
        stars[_start_row] += "*"
        stars[_start_row + 1] += "* *"
        stars[_start_row + 2] += "*****"
        return
    else:
        half_row_count = int(_row_count * 0.5)
        draw_triforce(_start_row, half_row_count)  # up
        draw_triforce(_start_row + half_row_count, half_row_count)  # left

        for i in range(0, half_row_count):
            stars[_start_row + half_row_count + i] += " " * (2 * (half_row_count-i) - 1)

        draw_triforce(_start_row + half_row_count, half_row_count)  # right
        return


draw_triforce(0, N)

for i in range(0, len(stars)):
    stars[i] += " " * (N - 1 - i)

    print(stars[i])
