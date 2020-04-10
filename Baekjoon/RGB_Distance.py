# 입력: 첫째 줄에 집의 수 N이 주어진다.
# N은 1,000보다 작거나 같다.
# 둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때, 초록으로 칠할 때, 파랑으로 칠할 때 드는 비용이 주어진다.
# 비용은 1,000보다 작거나 같은 자연수이다.
# 출력: 첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
cost = [[0, 0, 0] for i in range(0, N + 1)]
d = [[0, 0, 0] for i in range(0, N + 1)]
for i in range(1, N + 1):
    cost[i] = sys.stdin.readline().rstrip().split()
    for j in range(0, 3):
        cost[i][j] = int(cost[i][j])

# d[i][color_index]: i번째에 특정 색상(color_index)을 칠했을 때, i번째 집까지 칠할 때 드는 비용의 최소값
# cost[i][color_index]: i번째 집에 특정 색상(color_index)을 칠할 때 드는 비용

# d[i][color_index] = d[i-1][color_index] + min(cost[i][color_index])

for i in range(1, N + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + cost[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + cost[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + cost[i][2]

print(min(min(d[N][0], d[N][1]), d[N][2]))   # 찾는 값: min(d[i][0], d[i][1], di[i][2])
