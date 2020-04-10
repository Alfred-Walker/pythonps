# 입력
# 첫째 줄에 N이 주어진다.
# N은 항상 3의 제곱꼴인 수이다. (3, 9, 27, ...) (N=3k, 1 ≤ k < 8)
#
# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

# 27
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***   ***         ***   ***
# * *   * *         * *   * *
# ***   ***         ***   ***
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
import sys
sys.setrecursionlimit(10**8)


N = int(sys.stdin.readline().rstrip())
result = ["" for r in range(N)]


def set_star(row, size):
    if size == 3:
        result[row] += "***"
        result[row + 1] += "* *"
        result[row + 2] += "***"
        return

    size //= 3
    set_star(row, size)
    set_star(row, size)
    set_star(row, size)

    set_star(row + size, size)

    for i in range(size):
        result[row + size + i] += " " * size

    set_star(row + size, size)

    set_star(row + int(size << 1), size)
    set_star(row + int(size << 1), size)
    set_star(row + size << 1, size)


set_star(0, N)

print(*result, sep="\n")
