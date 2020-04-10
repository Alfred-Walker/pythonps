# 점수 중에 최댓값을 골라 이 값을 M이라고 한다.
# 그리고 나서 모든 점수를 점수/M*100으로 고친다.
# 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하라.
# 입력: 첫째 줄에 시험 본 과목의 개수 N이 주어진다.
# 이 값은 1000보다 작거나 같다.
# 둘째 줄에 현재 성적이 주어진다.
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 출력: 첫째 줄에 새로운 평균을 출력한다.
# 정답과의 절대/상대 오차는 10^-2까지 허용한다.
import sys

N = sys.stdin.readline().rstrip()
scores = sys.stdin.readline().rstrip().split()
M = 0
average = 0
for i in scores:
    if float(i) >= M:
        M = float(i)

for i in scores:
    average += float(i) / M * 100

print(average/float(N))
