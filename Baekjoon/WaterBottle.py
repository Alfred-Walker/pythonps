# 각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다.
# 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다.
# 이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데,
# 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
# 이 과정에서 손실되는 물은 없다고 가정한다.
#
# 이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다.
# 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 세 정수 A, B, C가 주어진다.
#
# 출력
# 첫째 줄에 공백으로 구분하여 답을 출력한다. 각 용량은 오름차순으로 정렬한다.

import sys
sys.setrecursionlimit(10**6)

A, B, C = map(int, sys.stdin.readline().rstrip().split())
answer = set()
checked = dict()


def pour_bottle(current):
    if tuple(current) in checked.keys():
        return

    if current[0] == 0:
        answer.add(current[2])
    checked[tuple(current)] = True
    next = current.copy()

    if current[0] > 0:
        # 1. A => B
        # print("A => B")
        next[0] = max(0, current[0] - (B - current[1]))
        next[1] = min(B, current[1] + current[0])
        next[2] = current[2]
        pour_bottle(next)

        # 2. A => C
        # print("A => C")
        next[0] = max(0, current[0] - (C - current[2]))
        next[1] = current[1]
        next[2] = min(C, current[2] + current[0])
        pour_bottle(next)

    if current[1] > 0:
        # 3. B => A
        # print("B => A")
        next[0] = min(A, current[0] + current[1])
        next[1] = max(0, current[1] - (A - current[0]))
        next[2] = current[2]
        pour_bottle(next)

        # 4. B => C
        # print("B => C")
        next[0] = current[0]
        next[1] = max(0, current[1] - (C - current[2]))
        next[2] = min(C, current[2] + current[1])
        pour_bottle(next)

    if current[2] > 0:
        # 5. C => A
        # print("C => A")
        next[0] = min(A, current[0] + current[2])
        next[1] = current[1]
        next[2] = max(0, current[2] - (A - current[0]))
        pour_bottle(next)

        # 6. C => B
        # print("C => B")
        next[0] = current[0]
        next[1] = min(B, current[1] + current[2])
        next[2] = max(0, current[2] - (B - current[1]))
        pour_bottle(next)

    return


pour_bottle([0, 0, C])
answer = sorted(answer)
print(*answer)
