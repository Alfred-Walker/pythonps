# 문제
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면
# y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

import sys


N = int(sys.stdin.readline().rstrip())
coordinates = [[0, 0] for i in range(N)]

for i in range(N):
    coordinates[i][0], coordinates[i][1] = map(int, sys.stdin.readline().split())

# lambda
# coordinates = sorted(coordinates, key=lambda coord: [coord[0], coord[1]])


# 퀵소트
def partition(left_index, right_index, list_to_sort):
    if left_index >= right_index:
        return

    pivot_index = left_index
    new_pivot_index = pivot_index
    for i in range(left_index + 1, right_index + 1):
        if list_to_sort[i][0] < list_to_sort[pivot_index][0]:
            new_pivot_index += 1
            list_to_sort[i], list_to_sort[new_pivot_index] = list_to_sort[new_pivot_index], list_to_sort[i]
        elif list_to_sort[i][0] == list_to_sort[pivot_index][0]:
            if list_to_sort[i][1] < list_to_sort[pivot_index][1]:
                new_pivot_index += 1
                list_to_sort[i], list_to_sort[new_pivot_index] = list_to_sort[new_pivot_index], list_to_sort[i]

    list_to_sort[pivot_index], list_to_sort[new_pivot_index] = list_to_sort[new_pivot_index], list_to_sort[pivot_index]

    return new_pivot_index


def quick_coord_sort(left_index, right_index, coord_list_to_sort):
    if left_index >= right_index:
        return

    pivot_index = partition(left_index, right_index, coord_list_to_sort)
    quick_coord_sort(left_index, pivot_index - 1, coord_list_to_sort)
    quick_coord_sort(pivot_index + 1, right_index, coord_list_to_sort)


quick_coord_sort(0, N - 1, coordinates)

for c in coordinates:
    print(*c)


'''
# selection sort - time up (N^2)
for i in range(N):
    min_index = i
    for j in range(i + 1, N):
        if coordinates[min_index][0] > coordinates[j][0]:
            min_index = j
        elif coordinates[min_index][0] == coordinates[j][0]:
            if coordinates[min_index][1] > coordinates[j][1]:
                min_index = j

    if i != min_index:
        coordinates[min_index], coordinates[i] = coordinates[i], coordinates[min_index]
'''