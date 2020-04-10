# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

# 입력: 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력: 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A = [0] + A     # 편의를 위해 0 추가
dp = [0] * (N + 1)  # dp[i]: i번째 원소를 끝으로 가지는 가장 긴 증가하는 부분 수열의 길이
dp[1] = 1
answer = dp[1]
for i in range(2, N + 1):
    longest = 0
    for j in range(1, i):
        if A[j] < A[i]:
            longest = max(longest, dp[j])

    dp[i] = longest + 1
    answer = max(answer, dp[i])

print(answer)
