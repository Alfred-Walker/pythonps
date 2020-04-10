# 입력
# 첫째 줄에 N이 주어진다. N은 항상 3×2^k 수이다. (3, 6, 12, 24, 48, ...) (k ≤ 10)
#
# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.
# 24
#                        *
#                       * *
#                      *****
#                     *     *
#                    * *   * *
#                   ***** *****
#                  *           *
#                 * *         * *
#                *****       *****
#               *     *     *     *
#              * *   * *   * *   * *
#             ***** ***** ***** *****
#            *                       *
#           * *                     * *
#          *****                   *****
#         *     *                 *     *
#        * *   * *               * *   * *
#       ***** *****             ***** *****
#      *           *           *           *
#     * *         * *         * *         * *
#    *****       *****       *****       *****
#   *     *     *     *     *     *     *     *
#  * *   * *   * *   * *   * *   * *   * *   * *
# ***** ***** ***** ***** ***** ***** ***** *****
import sys
sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline().rstrip())
stars = [""] * N


def set_tri(row, n):
    if n == 3:
        stars[row] += "*"
        stars[row + 1] += "* *"
        stars[row + 2] += "*****"
        return

    # top
    set_tri(row, n//2)
    # left, right
    set_tri(row + n//2, n//2)
    mid_chunk_length = n - 1
    for i in range(row + n//2, row + n):
        stars[i] += " " * mid_chunk_length + stars[i]
        mid_chunk_length -= 2

    return


set_tri(0, N)
for i in range(N):
    chunk = " " * (N - i - 1)
    stars[i] = chunk + stars[i] + chunk
print(*stars, sep="\n")
