# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에
# 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

# 입력: 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력: 첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.
import sys


N = int(sys.stdin.readline().rstrip())
dp = [0] * (1000 + 1)  # dp[i]: A의 i번째 항이 마지막 항인 A의 증가 부분 수열 중 가장 합이 큰 경우의 합
A = list(map(int, sys.stdin.readline().rstrip().split()))
A = [0] + A
dp[1] = A[1]
answer = A[1]

for i in range(2, N + 1):
    temp_sum = 0
    for j in range(1, i):
        if A[i] > A[j]:
            temp_sum = max(temp_sum, dp[j])

    dp[i] = temp_sum + A[i]
    answer = max(answer, dp[i])

print(answer)
