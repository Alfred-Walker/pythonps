# 문제
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있다.
# 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다.
# 입력으로 주어지는 수는 1000000을 넘지 않는다.
#
# 출력
# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
#
# 예제 입력 1
# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25
# 예제 출력 1
# 70
# 3
# 35

import sys


t = int(sys.stdin.readline().rstrip())
cases = []
for case in range(t):
    cases.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = []
memo = dict()


def get_gcd(a, b):
    if (a, b) in memo.keys():
        return memo[(a, b)]

    while a % b != 0:
        c = a % b
        a = b
        b = c

    memo[(a, b)] = b
    memo[(b, a)] = b

    return b


for case in cases:
    sum_gcd = 0
    for i in range(1, case[0] + 1):
        for j in range(i + 1, case[0] + 1):
            sum_gcd += get_gcd(case[i], case[j])

    answer.append(sum_gcd)

print(*answer, sep="\n")
