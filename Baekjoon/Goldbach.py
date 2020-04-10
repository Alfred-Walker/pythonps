# 골드바흐의 추측
# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
#
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.
# 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
#
# 이 추측은 아직도 해결되지 않은 문제이다.
#
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
#
# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.
# 테스트 케이스의 개수는 100,000개를 넘지 않는다.
#
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
# 입력의 마지막 줄에는 0이 하나 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.
# 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
# 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.
# 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.
#
# 예제 입력 1
# 8
# 20
# 42
# 0
# 예제 출력 1
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

import sys

is_prime_number = [True] * 1000001
is_prime_number[1] = False
cases = []
max_input = 0
while True:
    last_input = int(sys.stdin.readline().rstrip())

    if last_input != 0:
        cases.append(last_input)
        max_input = max(max_input, last_input)
    else:
        break

# 2부터 max_input의 루트값(포함)까지 범위에 대해 에라토스테네스의 체를 적용하여
# 미리 소수의 목록을 작성
for i in range(2, int(max_input**0.5) + 1):
    if is_prime_number[i]:
        for j in range(i*i, max_input + 1, i):
            is_prime_number[j] = False


def verify_goldbach(num):
    # num = a + b이고 a, b를 각각 2i+1, 2j+1 (i, j는 1 이상의 자연수) 라고 했을 때
    # 가장 작은 홀수는 3, 가장 큰 홀수는 num - 3이므로 i의 범위는 다음과 같다.
    # 1) 2i + 1이 가장 큰 홀수일 때 (num - 3 = 2i + 1)
    # 0.5 * (num - 4) = 0.5 * num - 2 = i
    # 2) 2i + 1이 가장 작은 홀수일 때 (3 = 2i + 1)
    # i = 1

    # 문제에서 b-a가 가장 큰 것을 요구하였으므로,
    # 가장 작은 a부터 탐색하여 가장 먼저 나오는 소수 a, b 조합을 답으로 출력
    for i in range(1, int(0.5 * num) - 2 + 1):
        a = 2 * i + 1
        b = num - a
        if is_prime_number[a] and is_prime_number[num - a]:
            return "{0} = {1} + {2}".format(num, a, b)

    # 소수 조합을 찾지 못하였을 때 출력
    return "Goldbach's conjecture is wrong."


for case in cases:
    print(verify_goldbach(case))
