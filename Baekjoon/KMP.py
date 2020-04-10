# https://www.acmicpc.net/problem/2902
# 입력: 입력은 한 줄로 이루어져 있고, 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈 ('-', 아스키코드 45)로만 이루어져 있다.
# 첫 번째 글자는 항상 대문자이다. 그리고, 하이픈 뒤에는 반드시 대문자이다. 그 외의 모든 문자는 모두 소문자이다.
# 출력: 첫 줄에 짧은 형태 이름을 출력한다.
import sys

inputs = sys.stdin.readline().rstrip().split('-')
answer = ""
for i in inputs:
    answer += i[0]

print(answer)
