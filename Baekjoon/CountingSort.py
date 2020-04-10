# 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys


N = int(sys.stdin.readline())
cnt = [0] * 10001

for i in range(0, N):
    cnt[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    print("%s\n" % i * cnt[i], end="")
