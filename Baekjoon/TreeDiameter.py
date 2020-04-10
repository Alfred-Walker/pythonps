# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
# 트리의 지름을 구하는 프로그램을 작성하시오.
#
# 입력
# 트리가 입력으로 주어진다.
# 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2≤V≤100,000)
# 둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다.
# (정점 번호는 1부터 V까지 매겨져 있다고 생각한다)
#
# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데,
# 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
# 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고,
# 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
# 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.
#
# 출력
# 첫째 줄에 트리의 지름을 출력한다.
import sys
sys.setrecursionlimit(10**6)


V = int(sys.stdin.readline().rstrip())
connected = [[]for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]

# 입력 처리
for i in range(1, V + 1):
    edges = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(edges)-1, 2):
        connected[edges[0]].append((edges[j], edges[j + 1]))
        # 오입력 주의: connected[i].append((edges[j], edges[j + 1]))


# v로부터 연결된 정점 중 방문하지 않은 곳들에 대하여 재귀.
# dist로 누적 거리를 체크
def dfs(v, dist):
    ret = (v, dist)
    visited[v] = True

    for v_d in connected[v]:
        if visited[v_d[0]]:
            continue

        next_search = dfs(v_d[0], dist + v_d[1])

        if ret[1] < next_search[1]:
            ret = next_search

    return ret


# 첫번째 dfs: 임의의 점(1)로부터 가장 먼 곳과 거리 구함
first_dfs = dfs(1, 0)
far_v = first_dfs[0]

# 다시 dfs 하기 위해 visited 초기화
visited = [False for _ in range(V + 1)]

# 두번째 dfs: 앞서 구한 1로부터 먼 곳에서 다시 가장 먼 곳을 찾음
second_dfs = dfs(far_v, 0)
far_v = second_dfs[1]
print(far_v)
