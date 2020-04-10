import collections
import sys

first_input = sys.stdin.readline().rstrip().split()
N = int(first_input[0])
L = int(first_input[1])
A = sys.stdin.readline().rstrip().split()
A = list(map(int, A))
D = []

deque = collections.deque()


def test(l):
    for index in range(1, N + 1):
        if index <= l:
            deque.append(A[index - 1])
            last_min = min(deque)
            D.append(last_min)
            continue
        else:
            removed = deque.popleft()
            added = A[index - 1]

            if added < last_min:
                last_min = added
            elif removed == last_min:
                last_min = min(deque)

            D.append(last_min)
            deque.append(added)


test(L)
print(*D)
