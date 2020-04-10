# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.
#
# 산술평균(arithmetic mean) : N개의 수들의 합을 N으로 나눈 값
# 중앙값(median) : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값(mode) : N개의 수들 중 가장 많이 나타나는 값
# 범위(range) : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력: 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import operator
import sys


N = int(sys.stdin.readline().rstrip())
nums = []
freq = {}
num_sum = 0

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    nums.append(n)
    num_sum += n
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

if N == 1:
    print(num_sum)
    print(num_sum)
    print(num_sum)
    print(0)
    exit(0)

nums.sort()
freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))

arithmetic_mean = round(num_sum / N)
median = nums[int(N >> 1)]
mode = freq[0][0]   # 유일한 최반값
if freq[0][1] == freq[1][1]:
    # 최빈값이 여러개일 경우
    mode = sorted(list(filter(lambda x: x[1] == freq[0][1], freq)))[1][0]

statistics_range = nums[N-1] - nums[0]

print(arithmetic_mean)
print(median)
print(mode)
print(statistics_range)
