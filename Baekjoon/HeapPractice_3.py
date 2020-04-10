class MinHeap:
    def __init__(self, arg_list=None):
        self.queue = [None]
        if arg_list is not None:
            self.queue += arg_list

    def last(self):
        return len(self.queue) - 1

    @staticmethod
    def parent(i):
        return i // 2

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

        if left <= self.last() and self.queue[i] > self.queue[left]:
            smallest = left

        if right <= self.last() and self.queue[i] > self.queue[right]:
            smallest = right

        if smallest != i:
            self.queue[smallest], self.queue[i] = self.queue[i], self.queue[smallest]
            self.min_heapify(smallest)

    def insert(self, n):
        self.queue.append(n)
        i = self.last()

        while i > 1:
            parent = self.parent(i)
            if self.queue[parent] > self.queue[i]:
                self.queue[parent], self.queue[i] = self.queue[i], self.queue[parent]
                i = parent
            else:
                break

    def delete(self):
        last = self.last()
        self.queue[1], self.queue[last] = self.queue[last], self.queue[1]
        self.queue.pop()

        for index in range(len(self.queue), 0, -1):
            self.min_heapify(index)


min_heap = MinHeap([3, 4, 22, 4])
print(min_heap.queue)
min_heap.delete()
print(min_heap.queue)
min_heap.insert(-1)
print(min_heap.queue)