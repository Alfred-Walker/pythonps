class MinHeap:
    def __init__(self, arg_list=None):
        self.queue = [0]
        if arg_list is not None:
            self.queue += arg_list
            for i in range(len(arg_list)//2, 0, -1):
                self.min_heapify(i)

    def last(self):
        return len(self.queue) - 1

    @staticmethod
    def parent(i):
        return i//2

    @staticmethod
    def left(i):
        return i * 2

    @staticmethod
    def right(i):
        return i * 2 + 1

    def min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left <= self.last() and self.queue[left] < self.queue[i]:
            smallest = left

        if right <= self.last() and self.queue[right] < self.queue[i]:
            smallest = right

        if self.queue[i] != self.queue[smallest]:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.min_heapify(smallest)

    def insert(self, n):
        self.queue.append(n)
        i = self.last()
        while i > 1:
            parent = self.parent(i)
            if self.queue[parent] > n:
                self.queue[parent], self.queue[i] = self.queue[i], self.queue[parent]
                i = parent
            else:
                break

    def delete(self):
        i = self.last()
        self.queue[1], self.queue[i] = self.queue[i], self.queue[1]
        self.queue.pop()
        self.min_heapify(1)


min_heap = MinHeap([4, 5, 3, 77, 2])
print(min_heap.queue)
min_heap.delete()
print(min_heap.queue)
min_heap.insert(-1)
print(min_heap.queue)