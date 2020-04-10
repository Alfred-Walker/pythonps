# 세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.
#
# 세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다.
# 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.
#
# 어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다.
# 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때,
# 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다.
# 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다.
# N과 M은 100보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다.
# 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.
#
# 출력
# 세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.
from sys import stdin

# 매우 느린 구현. RectDivision_2 에서 개선됨.
N, M = map(int, stdin.readline().rstrip().split())
nums = [[int(i) for i in stdin.readline().rstrip()] for n in range(N)]


def get_rect_sum(ri, ci, height, width):
    ret = 0
    # print("ri: {0} ci: {1} height: {2} width: {3}".format(ri, ci, height, width))

    for r in range(ri, ri + height):
        for c in range(ci, ci + width):
            ret += nums[r][c]

    return ret


def get_multi_of_sum(first_rect_height, first_rect_width):
    sum_first_rect = 0
    for ri in range(0, first_rect_height):
        for ci in range(0, first_rect_width):
            sum_first_rect += nums[ri][ci]

    ret = 0

    # 첫 사각형의 세로 길이가 N
    if first_rect_height == N:
        if first_rect_width == M:
            return 0

        # 1. 나머지 부분을 가로 2분할
        # 가운데 사각형 크기를 변경해나가며 비교
        for w_size in range(1, M - first_rect_width - 1 + 1):
            sum_mid = get_rect_sum(0, first_rect_width, N, w_size)
            sum_right = get_rect_sum(0, first_rect_width + w_size, N, M - w_size - first_rect_width)
            ret = max(ret, sum_first_rect * sum_mid * sum_right)

        # 2. 우측 나머지 부분을 세로 2분할
        # 우측 사각형 중 하나의 크기를 변경해나가며 비교
        for h_size in range(1, N):
            sum_top = get_rect_sum(0, first_rect_width, h_size, M - first_rect_width)
            sum_bottom = get_rect_sum(h_size, first_rect_width, N - h_size, M - first_rect_width)
            ret = max(ret, sum_first_rect * sum_top * sum_bottom)
    else:
        # 첫 사각형의 가로 길이가 M
        if first_rect_width == M:
            # 3. 세로 3등분
            # 가운데 사각형 크기를 변경해나가며 비교
            for h_size in range(1, N - first_rect_height - 1 + 1):
                sum_mid = get_rect_sum(first_rect_height, 0, h_size, M)
                sum_bottom = get_rect_sum(first_rect_height + h_size, 0, N - h_size - first_rect_height, M)
                ret = max(ret, sum_first_rect * sum_mid * sum_bottom)

            # 4. 첫 사각형 아래 영역을 2등분
            for w_size in range(1, M - 1 + 1):
                sum_left = get_rect_sum(first_rect_height, 0, N - first_rect_height, w_size)
                sum_right = get_rect_sum(first_rect_height, w_size, N - first_rect_height, M - w_size)
                ret = max(ret, sum_first_rect * sum_left * sum_right)
        else:
            # 5. 첫 사각형 위 영역을 2등분
            for w_size in range(1, M - 1 + 1):
                sum_left = get_rect_sum(first_rect_height, 0, N - first_rect_height, w_size)
                sum_right = get_rect_sum(first_rect_height, w_size, N - first_rect_height, M - w_size)
                ret = max(ret, sum_first_rect * sum_left * sum_right)

            # 6. 첫 사각형의 가로가 M보다 작고 세로가 N보다 작음
            # 6-1. 2가지 경우만 가능
            # 오른쪽의 세로길이가 N
            sum_bottom = get_rect_sum(first_rect_height, 0, N - first_rect_height, first_rect_width)
            sum_right = get_rect_sum(0, first_rect_width, N, M - first_rect_width)
            ret = max(ret, sum_first_rect * sum_bottom * sum_right)

            # 6-2. 아래의 가로길이가 M
            sum_bottom = get_rect_sum(first_rect_height, 0, N - first_rect_height, M)
            sum_right = get_rect_sum(0, first_rect_width, first_rect_height, M - first_rect_width)
            ret = max(ret, sum_first_rect * sum_bottom * sum_right)

    return ret


answer = 0

for h in range(1, N + 1):
    for w in range(1, M + 1):
        answer = max(answer, get_multi_of_sum(h, w))

print(answer)
