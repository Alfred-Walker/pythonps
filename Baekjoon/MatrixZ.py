# https://www.acmicpc.net/problem/1074

# 입력: 첫째 줄에 N r c가 주어진다.
# N은 15보다 작거나 같은 자연수이고,
# r과 c는 0보다 크거나 같고,2^N-1보다 작거나 같은 정수이다

# 출력: 첫째 줄에 문제의 정답을 출력한다.

import sys


def get_order(power, first_elem_row, first_elem_col, row, col):
    if power == 1:
        if first_elem_row == row:
            if first_elem_col == col:
                return 0
            else:
                return 1
        else:
            if first_elem_col == col:
                return 2
            else:
                return 3

    order = 0
    half_size = pow(2, power - 1)

    if row < first_elem_row + half_size:
        if col < first_elem_col + half_size:
            order += 0
            order += get_order(power - 1, first_elem_row, first_elem_col, row, col)
        else:
            order += half_size * half_size
            order += get_order(power - 1, first_elem_row, first_elem_col + half_size, row, col)
    else:
        if col < first_elem_col + half_size:
            order += half_size * half_size * 2
            order += get_order(power - 1, first_elem_row + half_size, first_elem_col, row, col)
        else:
            order += half_size * half_size * 3
            order += get_order(power - 1, first_elem_row + half_size, first_elem_col + half_size, row, col)

    return order


N, r, c = map(int, sys.stdin.readline().rstrip().split())
print(get_order(N, 0, 0, r, c))
