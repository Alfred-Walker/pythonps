# https://www.acmicpc.net/problem/2579

# 계단 오르는 데는 다음과 같은 규칙이 있다.
#
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

# 입력: 입력의 첫째 줄에 계단의 개수가 주어진다.
#
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
# 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# 출력: 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
import sys


N = int(sys.stdin.readline().rstrip())
scores = [int(sys.stdin.readline().rstrip()) for i in range(N)]
scores = [0] + scores
dp = [0] * (N + 1)      # dp[i]: i번째 계단을 마지막으로 밟았을 때 얻을 수 있는 총 점수의 최댓값
dp[1] = scores[1]
answer = dp[1]
for i in range(2, N + 1):
    max_score = 0
    max_score = max(max_score, dp[i-2] + scores[i])     # i번째 계단을 밟고 i-1번째 계단을 밟지 않고 i-2번째 계단을 밟는 경우.
    max_score = max(max_score, dp[i-3] + scores[i-1] + scores[i])     # i번째 계단을 밟고 i-1번째 계단을 밟고 i-2번째 계단을 밟지 않는 경우
    dp[i] = max_score

print(dp[N])
