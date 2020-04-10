# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
#
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
# {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
#
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다.
# (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

# 출력: 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A = [0] + A     # 편의를 위해 0 추가

dp = [0] * (N + 1)  # dp[i]: i번째 원소를 끝으로 가지는 가장 긴 감소 수열의 길이
dp_rev = [0] * (N + 1)  # dp_rev[i]: n-i+1번째 원소를 시작으로 가지는 가장 긴 감소 수열의 길이
dp[1] = 1
dp_rev[N-1+1] = 1

for i in range(2, N + 1):
    longest_inc = 0
    longest_dec = 0

    for j in range(1, i):
        if A[j] < A[i]:
            longest_inc = max(longest_inc, dp[j])

        if A[N-j+1] < A[N-i+1]:
            longest_dec = max(longest_dec, dp_rev[N-j+1])

    dp[i] = longest_inc + 1
    dp_rev[N - i + 1] = longest_dec + 1

answer = 0
for i in range(1, N + 1):
    #print("dp["+str(i)+"]: "+str(dp[i]) + ",  dp_rev["+str(i)+"]: "+str(dp_rev[i]))
    if dp[i] != 0 and dp_rev[i] != 0:
        answer = max(answer, dp[i] + dp_rev[i] - 1)
    else:
        answer = max(answer, dp[i] + dp_rev[i])

print(answer)
