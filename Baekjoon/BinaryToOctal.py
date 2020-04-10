# 문제
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
import sys


B = sys.stdin.readline().rstrip()
answer = ""

if B == '0':
    print(0)
    exit()

order = 0
split_per_three = 0
for i in range(len(B) - 1, -1, -1):
    split_per_three += int(B[i]) * 2 ** order

    if order == 3:
        answer = str(split_per_three % 8) + answer
        split_per_three = int(B[i])
        order = 0

    order += 1

if split_per_three != 0:
    answer = str(split_per_three % 8) + answer

print(answer)
