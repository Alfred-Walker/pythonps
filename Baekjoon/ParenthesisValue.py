# 개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서
# 올바른 괄호열이란 다음과 같이 정의된다.
#
# 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
# 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
# X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
# 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로  ‘(()[[ ]])’의 괄호값은 2×11=22 이다.
#  그리고  ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.
#
# 입력: 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
# 출력: 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
from collections import deque
import sys


stack = deque()
is_error = False

S = sys.stdin.readline().rstrip()
cnt_bracket = 0


for c in S:
    if c == "(":
        stack.append(c)
        cnt_bracket += 1
    elif c == "[":
        stack.append(c)
        cnt_bracket += 1
    elif c == ")":
        temp = 0
        cnt_bracket -= 1

        while len(stack) > 1 and type(stack[-1]) is int:
            temp += stack.pop()

        if len(stack) >= 1 and stack[-1] == "(":
            if temp == 0:
                temp = 2
            else:
                temp *= 2
            stack.pop()
            stack.append(temp)
        else:
            is_error = True
            break
    elif c == "]":
        temp = 0
        cnt_bracket -= 1

        while len(stack) > 1 and type(stack[-1]) is int:
            temp += stack.pop()

        if len(stack) >= 1 and stack[-1] == "[":
            if temp == 0:
                temp = 3
            else:
                temp *= 3
            stack.pop()
            stack.append(temp)
        else:
            is_error = True
            break
    else:
        is_error = True
        break

if cnt_bracket != 0 or is_error:
    print(0)
else:
    print(sum(stack))



# 위의 코드는 좋지못한 코드.
# value = {'(': 2, '[': 3, ')': 4, ']': 6}, 그리고 임시변수를 활용해서 다시 짜야.
# ]]] 등의 경우, [일 때만 넣도록 하면 무시할 수 있다.
# 스택에 괄호가 섞인 sum(stack)의 경우, try, except TypeError:로 걸러낼 수 있는 예외가 있다.
# 문제 시작시 괄호의 개수로 조기 진단할 수 있다 (len%2 == 0?)


# 1.   bracket 개수 검사
# 2.   for문으로 각 bracket 순회
# 2-1. [, (일 경우 처리
# 2-2. 그 외의 경우 처리 (while문 활용하여 스택이 빌 때까지 검사. [, (가 나오면 break)
# 2-2-1. ], )일 경우 처리 (, [의 값 두배가 ), ]임을 활용
# 2-2-2. 2-2-1. 외의 경우 처리 (숫자간의 덧셈. temp에 누적)
