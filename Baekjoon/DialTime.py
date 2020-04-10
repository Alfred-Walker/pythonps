# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
# 예를 들어, UNUCIC는 868242와 같다.

# 1
# ABC: 2
# DEF: 3
# GHI: 4
# JKL: 5
# MNO: 6
# PQRS: 7
# TUV: 8
# WXYZ: 9

# 입력: 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.

# 출력: 첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.
import sys


def get_time(_alphabet):
    if _alphabet in "ABC":
        return int(3)
    elif _alphabet in "DEF":
        return int(4)
    elif _alphabet in "GHI":
        return int(5)
    elif _alphabet in "JKL":
        return int(6)
    elif _alphabet in "MNO":
        return int(7)
    elif _alphabet in "PQRS":
        return int(8)
    elif _alphabet in "TUV":
        return int(9)
    elif _alphabet in "WXYZ":
        return int(10)


word = sys.stdin.readline().rstrip()
time = 0

for w in word:
    time += get_time(w)

print(time)
