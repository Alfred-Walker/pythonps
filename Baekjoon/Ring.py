# 상근이는 첫 번째 링을 돌리기 시작했고, 나머지 링도 같이 돌아간다는 사실을 발견했다.
# 나머지 링은 첫 번째 링 보다 빠르게 돌아가기도 했고, 느리게 돌아가기도 했다.
# 이렇게 링을 돌리다 보니 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 도는지 궁금해졌다.

# 링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)
# 다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다.
# 반지름은 1과 1000를 포함하는 사이의 자연수이다.

# 출력: 출력은 총 N-1줄을 해야 한다.
# 첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면
# 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.

import sys


def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


N = int(sys.stdin.readline().rstrip())
radius = [int(n) for n in sys.stdin.readline().rstrip().split()]

for i in range(1, N):
    temp = gcd(radius[0], radius[i])
    print(str(radius[0]//temp) + "/" + str(radius[i]//temp))
