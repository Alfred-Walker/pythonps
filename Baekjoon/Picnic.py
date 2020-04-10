# 입력: 입력의 첫 줄에는 테스트 케이스의 수 C(C<=50)가 주어진다.
# 각 테스트 케이스의 첫 줄에는 학생의 수 n(2<=n<=10)과 친구 쌍의 수 m(0<=m<=n(n-1)/2 이 주어진다.
# 그 다음 줄에는 m개의 정수 쌍으로 서로 친구인 두 학생의 번호가 주어진다.
# 번호는 모두 0부터 n-1사이의 정수이고, 같은 쌍은 입력에 두 번 주어지지 않는다.
# (학생들의 수는 짝수이다.)

# 출력: 각 테스트 케이스마다 한 줄에 모든 학생을 친구끼리만 짝지어줄 수 있는 방법의 수를 출력하라.

# 예시 입력 및 결과
# 3
# 2 1
# 0 1
# 4 6
# 0 1 1 2 2 3 3 0 0 2 1 3
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5


import sys

is_friend = [[False for i in range(10)] for j in range(10)]

n = 0


def count_pair(is_paired, depth):
    smallest_non_paired_index = -1
    for i in range(0, n):
        if is_paired[i] != 1:
            smallest_non_paired_index = i   # 중복을 피하기 위해 각 단계에서 가장 번호가 빠른 학생부터 짝을 지음
            break

    if smallest_non_paired_index == -1:     # paired all
        return 1

    ret = 0

    for i in range(smallest_non_paired_index + 1, n):
        if not is_paired[smallest_non_paired_index] and not is_paired[i] and is_friend[smallest_non_paired_index][i]:
            # print(str(smallest_non_paired_index) + " and " + str(i) + " is friend.")
            is_paired[smallest_non_paired_index], is_paired[i] = True, True
            ret += count_pair(is_paired[:], depth + 1)   # [:] call by value를 위해 리스트 복사
            is_paired[smallest_non_paired_index], is_paired[i] = False, False

    return ret


answer = []
C = int(sys.stdin.readline().rstrip())
for _ in range(C):
    # n: 학생의 수, m: 친구쌍의 수
    n, m = map(int, sys.stdin.readline().rstrip().split())
    my_is_paired = [False] * n
    is_friend = [[False for i in range(n)] for j in range(n)]

    pairs = sys.stdin.readline().rstrip().split()
    pairs = list(map(int, pairs))
    for p in range(0, m):
        p_0 = p * 2
        p_1 = p_0 + 1
        is_friend[pairs[p_0]][pairs[p_1]] = True
        is_friend[pairs[p_1]][pairs[p_0]] = True

    answer.append(count_pair(my_is_paired, 0))

print(*answer, sep="\n")
