# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다.
# 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
# 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.
# 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.
#
# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
# 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
#
# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수열의 크기 N이 주어진다. N은 10,000보다 작다.
# 둘째 줄부터 N개의 줄에, 수열의 각 수가 주어진다.
# 수열의 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
#
# 출력
# 수를 적절히 묶어 그 합이 최댓값을 출력한다.
# 정답은 항상 2^31보다 작다.
from sys import stdin


N = int(stdin.readline().rstrip())
positive = []
negative = []
zero_cnt = 0

for i in range(N):
    n = int(stdin.readline().rstrip())
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)
    else:
        zero_cnt += 1

positive.sort(reverse=True)
negative.sort()
answer = 0

# 양수가 홀수개인 경우 가장 작은 양수를 답에 추가
if len(positive) % 2 == 1:
    answer += positive.pop()

# 음수가 홀수개일 때 가장 큰 음수를 제거하거나 답에 추가
if zero_cnt > 0:
    # 가장 큰 음수를 제거
    if len(negative) % 2 == 1:
        negative.pop()
else:
    # 가장 큰 음수를 답에 더함
    if len(negative) % 2 == 1:
        answer += negative.pop()

# 양수 묶음들을 답에 추가 (2개씩 묶는 것에 주의)
for pi in range(0, len(positive), 2):
    # 1은 곱하지 않고 따로 더해주는 것이 더 큼에 유의
    if positive[pi + 1] == 1:
        answer += positive[pi] + 1
    else:
        answer += positive[pi] * positive[pi + 1]

# 음수 묶음들을 답에 추가 (2개씩 묶는 것에 주의)
for ni in range(0, len(negative), 2):
    answer += negative[ni] * negative[ni + 1]

print(answer)
