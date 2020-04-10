# 분수찾기
# https://www.acmicpc.net/problem/1193
# 입력: 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 출력: 첫째 줄에 분수를 출력한다.
import math
import sys


def get_fractional_number(x):
    n = math.ceil(math.sqrt(2 * x + 0.25) - 0.5)
    b = int(x - (n-1) * n/2)

    if n % 2 == 0:
        return str(b) + "/" + str(n - b + 1)
    else:
        return str(n - b + 1) + "/" + str(b)


X = int(sys.stdin.readline().rstrip())
print(get_fractional_number(X))
