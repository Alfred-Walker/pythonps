def dfs(i, computers, visited):
    cnt_node = len(computers)

    for j in range(cnt_node):
        if visited[j]:
            continue

        if computers[i][j] == 0:
            continue

        visited[j] = True
        dfs(j, computers, visited)


def solution(n, computers):
    answer = 0

    cnt_node = len(computers)

    visited = [False] * cnt_node
    for i in range(cnt_node):
        if visited[i]:
            continue

        # 첫 dfs 진입시 체크
        answer += 1
        visited[i] = True
        dfs(i, computers, visited)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))