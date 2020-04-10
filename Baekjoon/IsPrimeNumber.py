# 입력: 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 출력: 주어진 수들 중 소수의 개수를 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
inputList = [int(i) for i in (sys.stdin.readline().rstrip().split())]

for i in inputList:
    for j in range(2, i):
        if i % j is 0:
            N -= 1
            break;
    if i is 1:
        N -= 1

print(N)
