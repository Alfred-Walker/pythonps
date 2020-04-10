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
answer = 0
cnt_dict = dict()


# 1. 전체 부분집합을 A와 B 둘로 나누고, A의 부분집합의 합들을 먼저 구함
# 이 때 각 부분집합의 합이 몇번 나오는지 기록함
def get_sum_list(start, end, current_sum, sum_list):
    if start >= end:
        sum_list.append(current_sum)
        if current_sum in cnt_dict.keys():
            cnt_dict[current_sum] += 1
        else:
            cnt_dict[current_sum] = 1
        return

    get_sum_list(start + 1, end, current_sum + nums[start], sum_list)
    get_sum_list(start + 1, end, current_sum, sum_list)


# 2. B의 부분집합들의 합을 구할 때, (S - B의 합)인 값이 A의 합들을 구할 때
# 몇 번 나왔는지 확인함
def cnt_target_sum(target_sum, start, end, current_sum, sum_list):
    global answer

    if start >= end:
        diff = target_sum - current_sum
        if diff in cnt_dict.keys():
            answer += cnt_dict[diff]

        return

    cnt_target_sum(target_sum, start + 1, end, current_sum + nums[start], sum_list)
    cnt_target_sum(target_sum, start + 1, end, current_sum, sum_list)


get_sum_list(0, N//2, 0, left_sum_list)
cnt_target_sum(S, N//2, N, 0, left_sum_list)


# 공집합 제거 (문제의 조건 중 "길이가 양수인 부분수열 중에서" 에 해당)
if S == 0:
    answer -= 1

print(answer)
