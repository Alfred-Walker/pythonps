# 세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.
#
# 세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다.
# 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.
#
# 어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다.
# 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때,
# 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다.
# 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다.
# N과 M은 100보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다.
# 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.
#
# 출력
# 세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.
from sys import stdin


N, M = map(int, stdin.readline().rstrip().split())
nums = [[int(i) for i in stdin.readline().rstrip()] for n in range(N)]
total_sum = sum([sum(nums[n]) for n in range(N)])

answer = 0
# 4: 30
# A, B, C 세 부분으로 나누어 합을 구하고 그 곱을 비교.
# 1. 기준 사각형의 세로 길이가 N, 좌측에 위치하고 우측의 나머지 부분을 가로 2분할 (3등분)
A = B = C = 0
for i in range(0, M - 2):
    A += sum([nums[r][i] for r in range(0, N)])
    B = 0
    for j in range(i + 1, M - 1):
        B += sum([nums[r][j] for r in range(0, N)])
        C = total_sum - A - B
        answer = max(answer, A * B * C)


# 2. 기준 사각형의 세로 길이가 N, 좌측에 위치하고 우측 나머지 부분을 세로 2분할
A = B = C = 0
for i in range(0, M - 1):
    A += sum([nums[r][i] for r in range(0, N)])
    B = 0
    for j in range(0, N - 1):
        B += sum([nums[j][c] for c in range(i + 1, M)])
        C = total_sum - A - B
        answer = max(answer, A * B * C)


# 3. 기준 사각형의 가로 길이가 M, 위쪽에 위치하고 세로 3등분
A = B = C = 0
for i in range(0, N - 2):
    A += sum(nums[i])
    B = 0
    for j in range(i + 1, N - 1):
        B += sum(nums[j])
        C = total_sum - A - B
        answer = max(answer, A * B * C)


# 4. 기준 사각형의 가로 길이가 M, 위쪽에 위치하고 첫 사각형 아래 영역을 가로 2등분
A = B = C = 0
for i in range(0, N - 1):
    A += sum(nums[i])
    B = 0
    for j in range(0, M - 1):
        B += sum(nums[r][j] for r in range(i + 1, N))
        C = total_sum - A - B
        answer = max(answer, A * B * C)


# 5. 기준 사각형의 가로 길이가 M, 아래쪽에 위치하고 첫 사각형 위 영역을 가로 2등분
A = B = C = 0
for i in range(N - 1, 0, -1):
    A += sum(nums[i])
    B = 0
    for j in range(0, M - 1):
        B += sum(nums[r][j] for r in range(0, i))
        C = total_sum - A - B
        answer = max(answer, A * B * C)


# 6.기준 사각형의 세로 길이가 N, 우측에 위치하고 좌측의 나머지 부분을 세로 2분할
A = B = C = 0
for i in range(M - 1, 0, -1):
    A += sum([nums[r][i] for r in range(0, N)])
    B = 0
    for j in range(0, N - 1):
        B += sum([nums[j][c] for c in range(0, i)])
        C = total_sum - A - B
        answer = max(answer, A * B * C)


print(answer)
