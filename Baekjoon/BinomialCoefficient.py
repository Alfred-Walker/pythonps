# 자연수 N과 정수 K가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N과 K가 주어진다. (1≤N≤10, 0≤K≤N)
# 출력: 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
import math
import sys


N, K = map(int, sys.stdin.readline().rstrip().split())
print(int(math.factorial(N) / (math.factorial(K) * math.factorial(N - K))))

# nCk
N, K = map(int, sys.stdin.readline().rstrip().split())

# numerator - N * N -1... * N - (k - 1) == n! / (n - k)!
numerator = 1
for i in range(0, K):
    numerator *= N
    N -= 1

# denominator - K!
denominator = 1
for i in range(K, 0, -1):
    denominator *= i

print(numerator // denominator)
