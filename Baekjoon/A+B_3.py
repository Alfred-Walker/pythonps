# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
# (0 < A, B < 10)
# 출력: 각 테스트 케이스마다 A+B를 출력한다.
import sys

T = int(sys.stdin.readline().rstrip())
answer = [0]*T
for t in range(0, T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer[t] = a + b

print(*answer, sep="\n")
