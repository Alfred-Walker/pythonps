# 한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은
# A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)
# 을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다.
#
# 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때,
# A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.
#
# T(=5) = A[1] + B[1] + B[2]
#       = A[1] + A[2] + B[1]
#       = A[2] + B[3]
#       = A[2] + A[3] + B[1]
#       = A[3] + B[1] + B[2]
#       = A[3] + A[4] + B[3]
#       = A[4] + B[2]
# 입력
# 첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다.
# 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다.
# 다음 줄에는 m(1≤m≤1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다.
# 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.
#
# 출력
# 첫째 줄에 답을 출력한다.
# 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.
from sys import stdin


T = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))
M = int(stdin.readline().rstrip())
B = list(map(int, stdin.readline().rstrip().split()))


def get_subseq_sum_list(lis):
    ret = []
    for i in range(0, len(lis)):
        sub_sum = 0
        for j in range(i, len(lis)):
            sub_sum += lis[j]
            ret.append(sub_sum)

    return sorted(ret)


sub_a = get_subseq_sum_list(A)  # A나 B를 바로 사용하는 것이 아니라 subsequence의 합 목록을 구해야함
sub_b = get_subseq_sum_list(B)  # A나 B를 바로 사용하는 것이 아니라 subsequence의 합 목록을 구해야함
answer = 0
left = 0
right = len(sub_b) - 1      # right의 시작지점이 M -1 이 아닌 것에 주의!

while True:
    if left < len(sub_a) and right >= 0:
        total = sub_a[left] + sub_b[right]
    else:
        break

    if total == T:
        a_val = sub_a[left]
        b_val = sub_b[right]
        a_cnt = b_cnt = 0
        while True:
            if left < len(sub_a) and a_val == sub_a[left]:
                a_cnt += 1
                left += 1
            else:
                break

        while True:
            if right >= 0 and b_val == sub_b[right]:
                b_cnt += 1
                right -= 1
            else:
                break
        answer += a_cnt * b_cnt

    elif total < T:
        if left == len(sub_a) - 1:
            break

        left += 1
    else:
        if right == 0:
            break

        right -= 1


print(answer)
