# https://www.acmicpc.net/problem/10799
#
# 입력
# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.
#
# 출력
# 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
import collections
import sys


lasers_and_pipes = sys.stdin.readline().rstrip()
deque = collections.deque()

answer = 0
for lp in lasers_and_pipes:
    if lp == '(':
        deque.append(lp)
    elif lp == ')':
        if deque[-1] == '(':
            deque.pop()
            deque.append(1)
        else:
            laser_cnt = 0
            while deque[-1] != '(':
                laser_cnt += deque.pop()
            deque.pop()     # remove (
            answer += laser_cnt + 1
            deque.append(laser_cnt)

print(answer)
