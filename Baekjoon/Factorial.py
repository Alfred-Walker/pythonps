# 팩토리얼
# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
#
# 출력
# 첫째 줄에 N!을 출력한다.
import sys


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return factorial(n - 1) << 1
    elif n == 4:
        return factorial(n - 1) << 2
    elif n == 8:
        return factorial(n - 1) << 3
    else:
        return factorial(n - 1) * n


N = int(sys.stdin.readline().rstrip())
print(factorial(N))
