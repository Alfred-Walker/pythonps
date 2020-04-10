# * 숫자는 맞지만, 위치가 틀렸을 때는 볼
# * 숫자와 위치가 모두 맞을 때는 스트라이크
# * 숫자와 위치가 모두 틀렸을 때는 아웃
from itertools import permutations


def cnt_coincide(aaa, bbb):
    completely_same = 0
    val_only_same = 0

    for i in range(3):
        for j in range(3):
            if aaa[i] == bbb[j]:
                if i == j:
                    completely_same += 1
                else:
                    val_only_same += 1

    return completely_same, val_only_same


def solution(baseball):
    answer = 0
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    permu = list(map(''.join, permutations(nums, 3)))

    candidates = permu.copy()

    for b in baseball:
        if b[1] == 3:
            return 1

        for p in permu:
            cnt = cnt_coincide(str(b[0]), p)
            if cnt[0] != b[1] or cnt[1] != b[2]:
                if p in candidates:
                    candidates.remove(p)

    answer = len(candidates)

    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
