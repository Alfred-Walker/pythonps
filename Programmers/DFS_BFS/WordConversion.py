from collections import deque


def cnt_substring(a, b):
    cnt = 0

    for i in range(len(b)):
        if a[i] == b[i]:
            cnt += 1

    return cnt


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = []
    queue = deque()
    queue.append((begin, 0))

    while len(queue) != 0:
        q = queue.popleft()

        if q == target:
            return answer

        visited.append(q)

        for word in words:
            if cnt_substring(q[0], word) == len(q[0]) - 1:
                if word == target:
                    return q[1] + 1

                if word not in visited:
                    queue.append((word, q[1] + 1))

    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))