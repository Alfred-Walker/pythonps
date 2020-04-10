# 팩토리얼
import math


n = 10
factorial_n = math.factorial(n)

# -1, -2 등 - 인덱스로 거꾸로 탐색
test = [1, 2, 3]
print(test[-2])
# >>> 2





# 소인수분해
import sys


N = int(sys.stdin.readline().rstrip())

for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        print(i)
        N //= i

if N > 1:
    print(N)




# 에라토스테네스의 체
# N 제곱 + N 배로 소수의 배수들을 제외해나감
M, N = map(int, sys.stdin.readline().rstrip().split())
is_prime_number = [True] * 1000001
is_prime_number[1] = False


# 루트 포함하는 것에 주의
for i in range(2, int(N**0.5) + 1):
    if is_prime_number[i]:
        for j in range(i * i, N + 1, i):
            is_prime_number[j] = False
            j += i

for i in range(M, N + 1):
    if is_prime_number[i]:
        print(i)


