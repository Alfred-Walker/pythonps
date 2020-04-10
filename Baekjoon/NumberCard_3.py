# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가
# 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이가 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
# 이 수는 공백으로 구분되어져 있다. 이수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를
# 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

import sys


N = int(sys.stdin.readline().rstrip())
hold = list(map(int, sys.stdin.readline().rstrip().split()))
hold.sort()
M = int(sys.stdin.readline().rstrip())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []


def get_left_most(to_check, start, end):
    ret = -1
    while start <= end:
        mid = int((start + end) >> 1)

        if hold[mid] >= to_check:
            ret = mid
            end = mid - 1
        else:
            start = mid + 1

    return ret


def get_right_most(to_check, start, end):
    ret = -1
    while start <= end:
        mid = int((start + end) >> 1)

        if hold[mid] <= to_check:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1

    return ret


for card in check_list:
    li = get_left_most(card, 0, N - 1)
    ri = get_right_most(card, 0, N - 1)

    if li == -1 or ri == -1:
        answer.append(0)
    else:
        answer.append(ri - li + 1)

print(*answer)
