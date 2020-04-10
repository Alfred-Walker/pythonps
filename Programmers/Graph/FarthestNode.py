from collections import deque


def get_adjacent(n, edge):
    adjacent_list = dict()

    for i in range(1, n + 1):
        adjacent_list[i] = []

    for e in edge:
        start = e[0]
        end = e[1]
        if end not in adjacent_list[start]:
            adjacent_list[start].append(end)

        if start not in adjacent_list[end]:
            adjacent_list[end].append(start)

    return adjacent_list


def solution(n, edge):
    adjacent_list = get_adjacent(n, edge)
    min_dist = dict()

    queue = deque()
    queue.append((1, 0))

    visited = [False] * (n + 1)
    visited[1] = True

    while len(queue) != 0:
        q = queue.popleft()

        for adj in adjacent_list[q[0]]:
            if visited[adj]:
                continue

            dist = q[1] + 1
            min_dist[adj] = dist
            visited[adj] = True
            queue.append((adj, dist))

    # print(min_dist.items())
    sorted_list = sorted(min_dist.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_list)
    farthest = sorted_list[0][1]
    answer = 0
    for s in sorted_list:
        if s[1] == farthest:
            answer += 1
        else:
            break

    return answer


n = 5
edge = [[1, 4], [2, 3], [4,5]]
print(solution(n, edge))
