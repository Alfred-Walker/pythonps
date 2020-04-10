# 입력: 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
# 출력: 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

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


T = int(sys.stdin.readline().rstrip())
inputList = [None for i in range(0, T)]

for i in range(0, T):
    inputList[i] = sys.stdin.readline().rstrip().split()
    print(lcm(int(inputList[i][0]), int(inputList[i][1])))
