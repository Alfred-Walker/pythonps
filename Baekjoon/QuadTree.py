# 입력: 첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다.
# N 은 언제나 2의 제곱수로 주어지며, 1≤N ≤64의 범위를 가진다.
# 두 번째 줄부터는 길이 N 의 문자열이 N 개 들어온다.
# 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
# 출력: 영상을 압축한 결과를 출력한다.

import sys


def get_compressed(target, target_pow, first_elem_row, first_elem_col):
    if target_pow == 0:
        ret = target[first_elem_row][first_elem_col]
        return ret

    target_pow -= 1
    size = 2 ** target_pow

    ret = ""
    ret += get_compressed(target, target_pow, first_elem_row, first_elem_col)
    ret += get_compressed(target, target_pow, first_elem_row, first_elem_col + size)
    ret += get_compressed(target, target_pow, first_elem_row + size, first_elem_col)
    ret += get_compressed(target, target_pow, first_elem_row + size, first_elem_col + size)

    if ret == "0000":
        ret = "0"
    elif ret == "1111":
        ret = "1"

    if ret != "0" and ret != "1":
        ret = "(" + ret + ")"

    return ret


N = int(sys.stdin.readline().rstrip())
text = [sys.stdin.readline().rstrip() for i in range(N)]

pool = [2**i for i in range(0, 7)]
power = pool.index(N)
print(get_compressed(text, power, 0, 0))