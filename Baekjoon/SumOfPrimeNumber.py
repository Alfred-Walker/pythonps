# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
# 몇 가지 자연수의 예를 들어 보면 다음과 같다.
#
# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다.
# 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
# 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
#
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N이 주어진다.
# (1 ≤ N ≤ 4,000,000)
#
# 출력
# 첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
from sys import stdin


N = int(stdin.readline().rstrip())
is_prime = [True] * (N + 1)
is_prime[1] = 0
is_prime[1] = False


for i in range(2, int((N + 1) ** 0.5)):
    if is_prime[i]:
        for j in range(i * i, (N + 1), i):
            is_prime[j] = False


prime_seq = [p for p in range(2, N + 1) if is_prime[p]]
answer = left = right = 0
if len(prime_seq) != 0:
    current_sum = prime_seq[0]
else:
    current_sum = 0

while True:
    if left >= len(prime_seq) or right >= len(prime_seq):
        break

    if current_sum == N:
        answer += 1

    if current_sum <= N:
        right += 1
        if right < len(prime_seq):
            current_sum += prime_seq[right]
    else:
        current_sum -= prime_seq[left]
        left += 1

print(answer)
