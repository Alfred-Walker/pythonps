# https://www.acmicpc.net/problem/2632
# 피자가게에서 손님이 원하는 크기의 피자를 판매하는 모든 방법의 가지 수를 계산하는 프로그램을 작성하시오
# (한 종류의 피자를 2 조각 이상 판매할 때는 반드시 연속된 조각들을 잘라서 판매)
#
# 입력
# 첫 번째 줄에는 손님이 구매하고자 하는 피자크기를 나타내는 2,000,000 이하의 자연수가 주어진다.
# 두 번째 줄에는 A, B 피자의 피자조각의 개수를 나타내 는 정수 m, n 이 차례로 주어진다 ( 3≤m, n≤1000).
# 세 번째 줄부터 차례로 m 개의 줄에는 피자 A의 미리 잘라진 피자조각의 크기를 나타내는 정수가 주어진다.
# 그 다음 n 개의 줄에는 차례로 피자B의 미리 잘라진 피자조각의 크기를 나타내는 정수가 주어진다.
# 각 종류의 피자조각의 크기는 시계방향으로 차례로 주어지며, 각 피자 조각의 크기는 1000 이하의 자연수이다.
#
# 출력
# 첫째 줄에는 피자를 판매하는 방법의 가지 수를 나타내는 정수를 출력한다.
# 피자를 판매하는 방법이 없는 경우에는 숫자 0을 출력한다.
import sys
sys.setrecursionlimit(10**6)


P = int(sys.stdin.readline().rstrip())
M, N = map(int, sys.stdin.readline().rstrip().split())
A = [int(sys.stdin.readline().rstrip()) for a in range(M)]
B = [int(sys.stdin.readline().rstrip()) for b in range(N)]
sum_A, sum_B = dict(), dict()

answer = 0


def make_sum(index, current_piece, current_sum, target_sum, piece_list, sum_dict):
    if current_piece > len(piece_list):
        return
    if current_sum > target_sum:
        return

    if current_sum in sum_dict.keys():
        sum_dict[current_sum] += 1
    else:
        sum_dict[current_sum] = 1

    if index == len(piece_list):
        index = 0

    make_sum(index + 1, current_piece + 1, current_sum + piece_list[index], target_sum, piece_list, sum_dict)


for i in range(M):
    make_sum(i, 1, 0, P, A, sum_A)

for j in range(N):
    make_sum(j, 1, 0, P, B, sum_B)

sum_A[0], sum_B[0] = 1, 1
sum_A[sum(A)] = 1       # 모든 조각을 사용할 경우는 하나뿐이므로 중복 제거
sum_B[sum(B)] = 1       # make_sum 뒤에 불러줘야함 (관련 테스트 케이스: 6 \n 3, 3\n 1\n1\n1\n1\n1\n1)

for i in range(P + 1):
    if i in sum_A.keys() and (P - i) in sum_B.keys():
        answer += sum_A[i] * sum_B[P - i]

print(answer)
