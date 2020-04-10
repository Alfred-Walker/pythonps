# 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys


def insert_sort(_nums):
    for i in range(1, N):
        for j in reversed(range(0, i)):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                break


N = int(sys.stdin.readline().rstrip())
nums = [0 for i in range(0, N)]

for i in range(0, N):
    nums[i] = int(sys.stdin.readline().rstrip())

insert_sort(nums)
for i in range(0, N):
    print(nums[i])
