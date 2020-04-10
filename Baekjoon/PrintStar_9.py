# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
import sys


N = int(sys.stdin.readline().rstrip())
max_star_cnt = 2 * N - 1
stars = []

for i in reversed(range(2, N + 1)):
    star_cnt = 2 * i - 1
    left = " " * int((max_star_cnt - star_cnt) * 0.5)
    right = "*" * star_cnt
    stars.append(left + right)

for s in stars:
    print(s)

print(" " * (N - 1) + "*")

for s in reversed(stars):
    print(s)
