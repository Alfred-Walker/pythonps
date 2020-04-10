# 파이썬 heapq 사용
# 우선순위 큐와 연관 고려
import heapq

heap = []

# 원소 추가 (최소 힙)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
# >>> [1, 3, 7, 4]


# 원소 삭제 (최소 힙)
print(heapq.heappop(heap))
print(heap)
# >>> [3, 4, 7], 1이 삭제됨


# 기존 리스트를 힙으로 (최소 힙)
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)
# >>> [1, 3, 5, 4, 8, 7]


# 힙 정렬 (최소 힙)
def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))

    return sorted_nums


# 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것에 주의
# => heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]를 통해 새로운 최소값에 접근해야함


# 부모는 항상 자식 원소들보다 크기가 작거나 같음
# 자식 인덱스는 2k + 1, 2k + 2    (시작 인덱스 0)


