# N×N크기의 행렬로 표현되는 종이가 있다.
# 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다.
# 우리는 이 행렬을 적절한 크기로 자르려고 하는데,
# 이때 다음의 규칙에 따라 자르려고 한다.
#
# 1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고,
# 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수,
# 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 입력: 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다.
# 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

# 출력: 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를,
# 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
import sys


N = int(sys.stdin.readline().rstrip())
case = [list(map(int, sys.stdin.readline().rstrip().split())) for n in range(N)]
cnt = dict()
cnt[-1], cnt[0], cnt[1] = 0, 0, 0


def is_all_same(row, col, size):
    std = case[row][col]
    for r in range(size):
        for c in range(size):
            if case[row + r][col + c] != std:
                return False

    return True


def set_paper_cnt(row, col, size, result):
    if size == 1 or is_all_same(row, col, size):
        result[case[row][col]] += 1
    else:
        size //= 3
        for r in range(3):
            for c in range(3):
                set_paper_cnt(row + r * size, col + c * size, size, cnt)


set_paper_cnt(0, 0, N, cnt)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
