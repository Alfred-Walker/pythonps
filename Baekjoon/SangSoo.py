# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
# 예를 들어, 734과 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
# 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다.
# 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

# 출력: 첫째 줄에 상수의 대답을 출력한다.


# 파이썬의 자료형엔 크게 immutable(불변) 과 mutable(가변) 이 있다.
# int, str 같은 타입이 불변이고 list, dictionary 같은 타입이 mutable 이다.
# 불변 타입의 객체를 넘기면 call by value 가 되고 가변 타입의 객체를 넘기면 call by reference
# 출처: https://www.pymoon.com/entry/Python-은-callbyvalue-일까-callbyreference-일까 [인생 날로 먹기]


import sys

max_number = 0
numbers = sys.stdin.readline().rstrip().split()


def reversed_string(_str):
    temp = ""

    for j in reversed(range(0, len(_str))):
        temp += _str[j]

    return temp


for n in numbers:
    reversed_num = int(reversed_string(n))
    if max_number < reversed_num:
        max_number = reversed_num

print(max_number)
