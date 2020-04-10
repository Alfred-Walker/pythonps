# 입력: 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 출력: 첫째 줄에 (A+B)%C,
# 둘째 줄에 (A%C + B%C)%C,
# 셋째 줄에 (A×B)%C,
# 넷째 줄에 (A%C × B%C)%C를 출력한다.
A, B, C = input().split()
A, B, C = [int(A), int(B), int(C)]

valA = (A+B) % C
valB = (A % C + B % C) % C
valC = (A*B) % C
valD = ((A % C) * (B % C)) % C

print(valA)
print(valB)
print(valC)
print(valD)
