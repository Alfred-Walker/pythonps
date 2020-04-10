# 입력: 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다.
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
# x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 자연수는 2^31보다 작다.

# 출력: 입력에서 0이 주어진 회수만큼 답을 출력한다.
# 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
import sys


class MinHeap:
    def __init__(self):
        self.queue = [None]

    @staticmethod
    def left_child(index):
        return index * 2

    @staticmethod
    def right_child(index):
        return index * 2 + 1

    @staticmethod
    def parent(index):
        return int(index / 2)

    def delete(self):
        self.queue[1], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1], self.queue[1]
        self.queue.pop(len(self.queue) - 1)
        self.min_heapify(1)

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1  # last index

        while i > 1:
            parent = self.parent(i)
            if self.queue[parent] > self.queue[i]:
                self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
                i = parent
            else:
                break

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left <= len(self.queue) - 1 and self.queue[smallest] > self.queue[left]:     # child 존재 여부 체크
            smallest = left
        if right <= len(self.queue) - 1 and self.queue[smallest] > self.queue[right]:   # child 존재 여부 체크
            smallest = right
        if smallest != i:
            self.queue[smallest], self.queue[i] = self.queue[i], self.queue[smallest]
            self.min_heapify(smallest)


my_heap = MinHeap()
N = int(sys.stdin.readline().rstrip())
answer = []

for _ in range(0, N):
    X = int(sys.stdin.readline().rstrip())
    if X is 0:
        if len(my_heap.queue) < 2:
            answer.append(0)
        else:
            answer.append(my_heap.queue[1])
            my_heap.delete()
    else:
        my_heap.insert(X)

for _ in answer:
    print(_)
