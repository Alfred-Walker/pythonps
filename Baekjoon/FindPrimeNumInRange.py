# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#
# 예제 입력 1
# 3 16
# 예제 출력 1
# 3
# 5
# 7
# 11
# 13
import sys


M, N = map(int, sys.stdin.readline().rstrip().split())
is_prime_number = [True] * 1000001
is_prime_number[1] = False


for i in range(2, int(N**0.5) + 1):
    if is_prime_number[i]:
        for j in range(i * i, N + 1, i):
            is_prime_number[j] = False
            j += i

for i in range(M, N + 1):
    if is_prime_number[i]:
        print(i)
