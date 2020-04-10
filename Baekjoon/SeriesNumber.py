# 어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 출력: 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
import sys


def is_sequence(arg):
    if arg < 100:
        return 1

    t = int(arg / 10) % 10
    d = t - arg % 10    # very first diff
    arg = int(arg / 100)

    while arg != 0:
        new_t = arg % 10
        if d != (new_t - t):
            return 0
        t = new_t
        arg = int(arg / 10)
    return 1


N = int(sys.stdin.readline().rstrip())
answer = 0

for j in range(1, N+1):
    answer += is_sequence(j)

print(answer)
