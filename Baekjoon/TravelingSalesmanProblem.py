# 입력: 첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16)
# 다음 N개의 줄에는 비용 행렬이 주어진다.
# 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
# W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.
#
# 항상 순회할 수 있는 경우만 입력으로 주어진다.

# 출력: 첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
import sys


N = int(sys.stdin.readline().rstrip())
W = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
dp = [[-1 for i in range(1 << 16)] for j in range(N)]    # 2^16가지


def get_min_cost(size, cost_matrix, current_city, visited):
    if dp[current_city][visited] != -1:
        return dp[current_city][visited]

    if visited == (1 << N) - 1:
        if cost_matrix[current_city][0] != 0:
            return cost_matrix[current_city][0]
        else:
            return sys.maxsize

    ret = sys.maxsize

    for next_city in range(0, size):
        if (1 << next_city) & visited:
            continue

        if cost_matrix[current_city][next_city] == 0:
            continue

        visited = (1 << next_city) | visited

        # get_min_cost의 arg로 cost_matrix[current_city][next_city] 넘기지 말 것?
        cand = get_min_cost(size, cost_matrix, next_city, visited) + cost_matrix[current_city][next_city]

        ret = min(ret, cand)
        visited = ~(1 << next_city) & visited

    dp[current_city][visited] = ret

    return ret


# 순회하는 경로를 찾는 것이기 때문에 무조건 0번 도시에서 출발한다고 가정해도 총 경로의 길이는 동일
visited_city = 1    # 000....1 (0번째 자리가 1)
min_cost = get_min_cost(N, W, 0, visited_city)
print(min_cost)