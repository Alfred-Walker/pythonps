class MinHeap:
    def __init__(self, arg_list=None):
        if arg_list is not None:
            self.queue = [None]+arg_list        # 리스트를 사용한 초기화. 0번 인덱스를 비우고 복사해온 리스트 A와 합침
            for index in range(len(arg_list)//2, 0, -1):    # 범위 명시 주의
                self.min_heapify(index)
        else:
            self.queue = [None]

    # 왜 파이챰이 staticmethod를 제안하는가?
    # method 내에서 self를 사용하지 않기 때문에
    # class 인스턴스에 영향을 주지 않기 때문.

    def last(self):
        return len(self.queue) - 1

    @staticmethod
    def left(index):
        return index * 2

    @staticmethod
    def right(index):
        return index * 2 + 1

    @staticmethod
    def parent(index):
        return index // 2

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1     # 마지막 인덱스
        while i > 1:                # root로 오거나 멈출 때까지 매번 부모와 비교
            parent = self.parent(i)
            if self.queue[parent] > n:
                self.queue[parent], self.queue[i] = self.queue[i], self.queue[parent]
                i = parent
            else:                   # 만약 부모가 더 작으면 거기서 끝
                break

    def delete(self):
        last = self.last()
        self.queue[1], self.queue[last] = self.queue[last], self.queue[1]
        self.queue.pop(last)
        self.min_heapify(1)     # 루트에서 heapify 시작

    def min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i    # 가장 작은 것을 자신으로 놓고
        # 만약 왼쪽 자식이 존재하고(왼쪽 자식의 index가 마지막 인덱스보다 작거나 같고)
        # 동시에 smallest보다 작을 경우
        if left <= self.last() and self.queue[left] < self.queue[smallest]:
            smallest = left

        # 만약 왼쪽 자식이 존재하고(왼쪽 자식의 index가 마지막 인덱스보다 작거나 같고)
        # 동시에 smallest보다 작을 경우
        if right <= self.last() and self.queue[right] < self.queue[smallest]:
            smallest = right

        # 위의 두 비교 결과 가장 작은 것이 자기 자신이 아니었다면 스왑
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.min_heapify(smallest)  # smallest(left나 right)에 들어간 새 값에 대해 다시 min_heapify


min_heap = MinHeap()
for i in range(10):
    min_heap.insert([10 - i])

print(min_heap.queue)

test_list = [99, 98, 97, 96, 94, 32]
min_heap_by_list = MinHeap(test_list)
print(min_heap_by_list.queue)
print(test_list)
