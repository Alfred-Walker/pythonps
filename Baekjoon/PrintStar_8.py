# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
import sys


N = int(sys.stdin.readline().rstrip())
max_star_cnt = 2 * N - 1
stars = []

for i in range(1, N):
    star_cnt = i
    left = "*" * star_cnt
    center = " " * (2 * (N - star_cnt))
    right = left
    stars.append(left + center + right)

for s in stars:
    print(s)

print("*" * (2 * N))

for s in reversed(stars):
    print(s)
