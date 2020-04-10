# 문제
# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다.
# 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다.
# 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 같은 점이 여러 번 주어질 수도 있다.
#
# 출력
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.

# n lg^2 n 방식
import sys


def squared_dist(coord_a, coord_b):
    return (coord_b[0] - coord_a[0]) ** 2 + (coord_b[1] - coord_a[1]) ** 2


# 첫 호출 전에 coords는 x좌표로 정렬되어있어야함
def get_closest_dist(coords, start, end):
    if start == end:
        return sys.maxsize

    mid = (start + end)//2
    d_left = get_closest_dist(coords, start, mid)       # 좌측 영역에서 두 점을 골랐을 때 최소 거리(의 제곱, 제곱은 문제 요구사항)
    d_right = get_closest_dist(coords, mid + 1, end)    # 우측 영역에서 두 점을 골랐을 때 최소 거리(의 제곱, 제곱은 문제 요구사항)
    d = min(d_left, d_right)

    mid_x = (coords[mid - 1][0] + coords[mid + 1][0]) // 2

    candidates = []
    for i in range(start, end + 1):
        diff = coords[i][0] - mid_x
        if diff * diff <= d:                # diff 제곱과 비교하는 것에 주의. diff <= d ** 0.5는 시간초과
            candidates.append(coords[i])

    # y좌표 기준 정렬
    candidates.sort(key=lambda can: can[1])

    # 후보들 중 아래쪽부터 그 위의 점들과 비교
    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            if candidates[j][1] - candidates[i][1] > d:
                break
            d = min(d, squared_dist(candidates[i], candidates[j]))

    return d


N = int(sys.stdin.readline().rstrip())

# set가 아닌 list를 사용할 경우, pypy3도 시간초과.
# coord = [None] * N
# for n in range(N):
#     coord[n] = tuple(map(int, sys.stdin.readline().rstrip().split()))

coord = set([])
for n in range(N):
    coord.add(tuple(map(int, sys.stdin.readline().rstrip().split())))

coord = list(coord)

# x좌표 기준 정렬
coord.sort(key=lambda x: x[0])

answer = int(get_closest_dist(coord, 0, len(coord) - 1))
if answer == sys.maxsize:
    print(0)
else:
    print(answer)
