# 입력: 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.
# 출력: 첫째 줄에는 A×B×C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A×B×C의 결과에
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()

AxBxC = int(A) * int(B) * int(C)
AxBxC = str(AxBxC)
answer = [0]*10

for i in AxBxC:
    answer[int(i)] += 1

for i in answer:
    print(i)
