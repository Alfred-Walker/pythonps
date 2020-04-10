import sys


N = int(sys.stdin.readline().rstrip())
W = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
dp = [[-1 for i in range(1 << 16)]for j in range(N)]


def get_min_cost(size, cost_matrix, current_city, visited, current_cost):
    if dp[current_city][visited] != -1:
        return dp[current_city][visited]

    if visited == (1 << N) - 1:
        if cost_matrix[current_city][0] != 0:
            return current_cost + cost_matrix[current_city][0]
        else:
            return sys.maxsize

    ret = sys.maxsize

    for next_city in range(0, size):
        if (1 << next_city) & visited:
            continue

        if cost_matrix[current_city][next_city] == 0:
            continue

        visited = (1 << next_city) | visited

        # 잘못된 부분
        # dp테이블을 참조할 경우 (get_min_cost 첫부분) 전후 둘다 dp 테이블 값을 get_min_cost로 받아오는데
        # 이 때  + cost_matrix[current_city][next_city] 부분이 무시되고 현재 위치가 next_city일 때 남은 도시를 순회하는
        # 최저 비용만 dp를 통해 얻게 되어 정답이 아니게 된다.
        # 따라서 dp를 확인하는 부분에서 다음 줄의 + cost_matrix[current_city][next_city]를 같이 처리해주거나
        # 다음 줄에서 + cost_matrix[current_city][next_city] 부분을 arg 밖으로 빼내야 한다.
        cand = get_min_cost(size, cost_matrix, next_city, visited, current_cost + cost_matrix[current_city][next_city])

        ret = min(ret, cand)
        visited = ~(1 << next_city) & visited

    dp[current_city][visited] = ret
    return ret


# 순회하는 경로를 찾는 것이기 때문에 무조건 0번 도시에서 출발한다고 가정해도 총 경로의 길이는 동일
visited_city = 1
min_cost = get_min_cost(N, W, 0, visited_city, 0)

print(min_cost)
