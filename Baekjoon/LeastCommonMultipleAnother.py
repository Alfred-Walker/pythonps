# 입력: 한 줄에 두 정수 A와 B가 공백으로 분리되어 주어진다.
# 50%의 입력 중 A와 B는 1000(103)보다 작다. 다른 50%의 입력은 1000보다 크고 100000000(108)보다 작다.
# 추가: 큰 수 입력에 대하여 변수를 64비트 정수로 선언하시오.
# C/C++에서는 long long int를 사용하고, Java에서는 long을 사용하시오.

# 출력: A와 B의 최소공배수를 한 줄에 출력한다.

# 최대공약수(general common divisor)를 구하는 함수가 gcd(a,b) 일 때
# a mod b = 0 이라면 gcd(a, b) = b가 성립
# a mod b != 0 이라면 gcd(a, b) = gcd(b, a mod b)임이 성립한다. (유클리드 호제법)

import sys


def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


inputs = sys.stdin.readline().rstrip().split()
print(lcm(int(inputs[0]), int(inputs[1])))
