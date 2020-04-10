# 파이썬 heapq 사용
# 우선순위 큐와 연관 고려
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

# 원소 추가 (최대 힙)
# 각 값에 대한 우선순위를 구해 (우선순위, 값) 구조의 tuple 을 힙에 추가하거나 삭제
for num in nums:
    heapq.heappush(heap, (-num, num))     # (우선순위, 값)

while heap:
    print(heapq.heappop(heap)[1])

# >>> [1, 3, 7, 4]

# 힙 정렬 (최대 힙)
def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap)[1])

    return sorted_nums


print(heap_sort([5,8,3,4,2]))

# 인덱스 0에 가장 큰 원소가 있다고 해서, 인덱스 1에 두번째 큰 원소, 인덱스 2에 세번째 큰 원소가 있다는 보장은 없다는 것에 주의
# => heappop()을 통해 가장 큰 원소를 삭제 후에 heap[0]를 통해 새로운 최대값에 접근해야함

# 부모는 항상 자식 원소들보다 크기가 크거나 같음
# 자식 인덱스는 2k + 1, 2k + 2    (시작 인덱스 0)
