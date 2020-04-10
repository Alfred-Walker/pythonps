# 입력: 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가  빈칸을 사이에 두고 주어진다.
# 출력: 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를  도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.
import sys

yut = [[0] * 4] * 3
score = [""] * 3

for i in range(0, 3):
    yut[i] = sys.stdin.readline().rstrip().split()
    front_count = 0
    for y in yut[i]:
        front_count += int(y)

    if front_count is 0:
        score[i] = "D"
    elif front_count is 1:
        score[i] = "C"
    elif front_count is 2:
        score[i] = "B"
    elif front_count is 3:
        score[i] = "A"
    elif front_count is 4:
        score[i] = "E"

for i in score:
    print(i)
