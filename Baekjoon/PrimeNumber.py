# 입력: 첫 줄에 수의 개수 N이 주어진다.
# N은 100이하이다.
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력: 주어진 수들 중 소수의 개수를 출력한다.

import sys

untested = [n for n in range(2, 1001)]
non_prime_numbers = set([1])
prime_numbers = set([])


def check_prime_num(target):
    if target in prime_numbers:
        return True

    if target in non_prime_numbers:
        return False

    for t in range(2, int(target ** 0.5) + 1):
        if target % t == 0:
            non_prime_numbers.add(target)
            untested.remove(target)

            for j in range(target + target, 1000, target):
                non_prime_numbers.add(j)

            return False

    prime_numbers.add(target)

    for j in range(target + target, 1000, target):
        non_prime_numbers.add(j)

    return True


N = int(sys.stdin.readline().rstrip())
inputs = [int(i) for i in sys.stdin.readline().rstrip().split()]
answer = 0

for i in inputs:
    if check_prime_num(i):
        answer += 1

print(answer)

