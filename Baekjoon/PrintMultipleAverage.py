# 입력: 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력: 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
import sys

C = int(sys.stdin.readline().rstrip())
answer = []
for i in range(0, C):
    temp = 0
    arg = sys.stdin.readline().rstrip().split()
    n = float(arg[0])
    average = 0
    for j in range(1, len(arg)):
        average += float(arg[int(j)])
    average = average / n
    for j in range(1, len(arg)):
        if float(arg[int(j)]) > average:
            temp += 1

    # ver. 1
    answer.append(temp / n)

    # ver. 2
    # answer.append(round(temp / n * 100, 3))

# print ver 1.
for i in answer:
    print("{:.3%}".format(round(i, 5)))

# print ver 2.
# for i in answer:
    # print("{:.3f}".format(i)+"%")
