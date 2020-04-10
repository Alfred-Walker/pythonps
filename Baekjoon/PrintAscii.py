# 입력: 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# 출력: 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
import sys

N = sys.stdin.readline().rstrip()
print(ord(N))
