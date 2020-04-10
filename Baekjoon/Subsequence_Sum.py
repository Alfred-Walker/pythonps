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
answer = 0


def sub_sums(arg_index, arg_sum):
    global answer
    if arg_index >= N:
        if arg_sum == S:
            answer += 1
        return

    sub_sums(arg_index + 1, arg_sum)
    sub_sums(arg_index + 1, arg_sum + nums[arg_index])


sub_sums(0, 0)

# 공집합 제거 (문제의 조건 중 "길이가 양수인 부분수열 중에서" 에 해당)
if S == 0:
    answer -= 1

print(answer)
