# 입력: 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 출력: 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
digits = []
while N != 0:
    digits.append(N % 10)
    N = int(N * 0.1)

digits.sort(reverse=True)
print(*digits, sep="")
