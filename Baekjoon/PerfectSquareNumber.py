# 입력: 첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.
# 출력: M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.
import math
import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
sumOfSquareNum = 0
minSquareNum = N
for i in range(M, N+1):
    t = int(math.sqrt(i))   # t = int(i**0.5)
    if t * t == i:
        sumOfSquareNum += i
        if i < minSquareNum:
            minSquareNum = i

if sumOfSquareNum is 0:
    print(-1)
else:
    print(sumOfSquareNum)
    print(minSquareNum)
