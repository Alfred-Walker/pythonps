# 입력: 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
# 출력: 두 번째로 큰 정수를 출력한다.
import sys

A, B, C = sys.stdin.readline().rstrip().split()
A, B, C = [int(A), int(B), int(C)]

answer = A

if A >= B:
    if A >= C:
        if B >= C:
            answer = B
        else:
            answer = C
else:
    if B >= C:
        if A < C:
            answer = C
    else:
        answer = B

print(answer)