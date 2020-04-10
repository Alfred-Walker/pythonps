# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다.
# 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다.
# 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다.

from sys import stdin


N, M = map(int, stdin.readline().rstrip().split())
A = list(map(int, stdin.readline().rstrip().split()))

left = 0
right = 0
total = 0
answer = 0

# while right < N: <= 오답
while True:
    if total <= M:
        # 부분합이 M보다 작거나 같은 경우
        if right == N:  # 중요. right를 증가시켜야할 때 값 체크.
            break
        total += A[right]
        right += 1
    else:
        # 부분합이 M보다 큰 경우
        total -= A[left]
        left += 1

    # 제일 앞에 와도 무관
    if total == M:
        answer += 1

print(answer)
