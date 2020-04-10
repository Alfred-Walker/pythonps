# N개의 정수로 이루어진 배열 A가 주어진다.
# 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
#
# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다.
# 둘째 줄에는 배열 A에 들어있는 정수가 주어진다.
# 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
from sys import stdin


def permutation(lst):
    # 빈 리스트 => 순열이 없음
    if len(lst) == 0:
        return []

    # 한개의 순열만이 가능
    if len(lst) == 1:
        return [lst]

    # 길이가 1개 이상의 순열을 찾음
    ret = []  # 현재 순열을 저장할 빈 리스트

    for i in range(len(lst)):
        m = lst[i]

        # m을 제외한 리스트 생성
        remain_list = lst[:i] + lst[i + 1:]

        # m으로 시작하는 모든 순열의 리스트 생성
        for p in permutation(remain_list):
            ret.append([m] + p)
    return ret


N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))
permutations = permutation(A)

answer = 0

for p in permutations:
    p_sum = 0
    for i in range(N - 1):
        p_sum += abs(p[i] - p[i + 1])

    answer = max(answer, p_sum)

print(answer)
