# 문제
# 문자열 N개가 주어진다.
# 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
#
# 입력
# 첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100)
# 문자열의 길이는 100을 넘지 않는다.
#
# 출력
# 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
import sys

lines = []
for line in sys.stdin:
    if line == "\n":
        break

    lines.append(line)

for l in lines:
    answer = [0, 0, 0, 0]
    for s in l:
        ascii_s = ord(s)

        if ord('a') <= ascii_s <= ord('z'):
            answer[0] += 1
        elif ord('A') <= ascii_s <= ord('Z'):
            answer[1] += 1
        elif ord('0') <= ascii_s <= ord('9'):
            answer[2] += 1
        elif ascii_s == ord(' '):
            answer[3] += 1

    print(*answer)
