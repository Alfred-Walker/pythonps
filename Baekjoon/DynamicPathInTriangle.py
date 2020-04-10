# https://www.acmicpc.net/problem/1932
#
# 입력: 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
# 출력: 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
import sys


n = int(sys.stdin.readline().rstrip())
numbers = [[0]]     # 편의를 위해 미사용 0 번째줄 추가
for _ in range(0, n):
    numbers.append(sys.stdin.readline().rstrip().split())

# i >= 1, j >= 1일 때
# d[i][j]
# 1) j == 1일 때
# d[i][j] = i-1번째 층에서 첫번째 수를 선택했을 경우 경로들의 최대합
# d[i][j] = d[i-1][1] + numbers[i][j-1]

# 2) j == i일 때
# d[i][j] = i-1번째 층에서 마지막 수를 선택했을 경우 경로들의 최대합
# d[i][j] = d[i-1][i-1] + numbers[i][j-1]

# 3) 1<j<i
# d[i][j] = i-1번째 층에서 j-1번째, 혹은 j번째 수를 선택했을 경우 나올 수 있는 경로들의 최대합
# d[i][j] = max(d[i-1][j-1], d[i-1][j]) + numbers[i][j-1]

# i: 0 <= i < n + 1 (n + 1개)
# j: 0 <= i < n + 3 (n + 3개)
d = [[0 for j in range(0, i + 2)] for i in range(0, n+1)]
max_d = 0

# print(*d)

for i in range(1, n+1):
    for j in range(1, i + 1):
        if j == 1:
            d[i][j] = d[i - 1][1] + int(numbers[i][j - 1])
        elif j == i:
            d[i][j] = d[i - 1][i - 1] + int(numbers[i][j - 1])
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + int(numbers[i][j - 1])

        if d[i][j] > max_d:
            max_d = d[i][j]

# print(*d, sep="\n")
print(max_d)
