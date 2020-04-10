# 입력: 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력: 첫째 줄에 A+B, 둘째 줄에 A-B,
# 셋째 줄에 A*B, 넷째 줄에 A/B,
# 다섯째 줄에 A%B를 출력한다.

A, B = input().split()
A, B = [int(A), int(B)]

valA = A + B
valB = A - B
valC = A * B
valD = A / B
valE = A % B

print(valA)
print(valB)
print(valC)
print(int(valD))
print(valE)
