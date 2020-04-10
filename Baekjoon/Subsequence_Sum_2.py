# N개의 정수로 이루어진 수열이 있을 때, 길이가 양수인 부분수열 중에서
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다.
# (1 ≤ N ≤ 40, |S| ≤ 1,000,000)
#
# 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
# 주어지는 정수의 절댓값은 100,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
from sys import stdin


N, S = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))
left_sum_list = []
right_sum_list = []
answer = 0


def get_sum_list(start, end, current_sum, sum_list):
    if start >= end:
        sum_list.append(current_sum)
        return

    get_sum_list(start + 1, end, current_sum + nums[start], sum_list)
    get_sum_list(start + 1, end, current_sum, sum_list)


get_sum_list(0, N//2, 0, left_sum_list)
get_sum_list(N//2, N, 0, right_sum_list)

left_sum_list.sort()
right_sum_list.sort()

li = 0
ri = len(right_sum_list) - 1

while li < len(left_sum_list) and ri >= 0:
    left_value = left_sum_list[li]
    right_value = right_sum_list[ri]

    s = left_value + right_value
    if s == S:
        left_cnt = 0
        right_cnt = 0
        while li < len(left_sum_list) and left_sum_list[li] == left_value:
            left_cnt += 1
            li += 1

        while ri >= 0 and right_sum_list[ri] == right_value:
            right_cnt += 1
            ri -= 1

        answer += (left_cnt * right_cnt)
    elif s > S:
        ri -= 1
    elif s < S:
        li += 1


# 공집합 제거 (문제의 조건 중 "길이가 양수인 부분수열 중에서" 에 해당)
if S == 0:
    answer -= 1

print(answer)
