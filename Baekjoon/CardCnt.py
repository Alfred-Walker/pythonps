# 문제
# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데,
# 적혀있는 수는 -2^62보다 크거나 같고, 2^62보다 작거나 같다.
#
# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
#
# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 <= N <= 1000000)이 주어진다.
# 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
#
# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.
import sys


N = int(sys.stdin.readline().rstrip())
nums = dict()
for _ in range(N):
    new = int(sys.stdin.readline().rstrip())
    if nums.get(new) is None:
        nums[new] = 1
    else:
        nums[new] += 1

nums = list(nums.items())

nums.sort(key=lambda x: (-x[1], x[0]))
print(nums[0][0])

'''
# 퀵소트
def partition(left_index, right_index, to_sort):
    if left_index >= right_index:
        return

    pivot_index = left_index
    new_pivot_index = pivot_index
    for i in range(left_index + 1, right_index + 1):
        if to_sort[i][1] < to_sort[pivot_index][1]:
            new_pivot_index += 1
            to_sort[i], to_sort[new_pivot_index] = to_sort[new_pivot_index], to_sort[i]
        elif to_sort[i][1] == to_sort[pivot_index][1]:
            if to_sort[i][0] > to_sort[pivot_index][0]:
                new_pivot_index += 1
                to_sort[i], to_sort[new_pivot_index] = to_sort[new_pivot_index], to_sort[i]

    to_sort[pivot_index], to_sort[new_pivot_index] = to_sort[new_pivot_index], to_sort[pivot_index]

    return new_pivot_index


def quick_card_sort(left_index, right_index, card_cnt_to_sort):
    if left_index >= right_index:
        return

    pivot_index = partition(left_index, right_index, card_cnt_to_sort)
    quick_card_sort(pivot_index + 1, right_index, card_cnt_to_sort)


quick_card_sort(0, len(nums) - 1, nums)
print(nums[-1][0])
'''