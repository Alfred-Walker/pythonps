# 문제
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의들에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
#
# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.

from sys import stdin


def is_collapsed(a, b):
    if a == b:
        # e.g. a(0, 0)과 b(0, 0), a(4, 4)와 b(4,4)등
        if a[0] == a[1]:
            return False
        # e.g. a(0, 3)과 b(0, 3), a(1, 4)와 b(1,4)등
        else:
            return True
    else:
        # range를 쓸 경우, range(1,0) = [] 임에 주의
        if (b[0] < a[0] < b[1]) or (b[0] < a[1] < b[1]) or (a[0] < b[0] < a[1]) or (a[0] < b[1] < a[1]):
            return True
        else:
            return False


N = int(stdin.readline().rstrip())
time = [tuple(map(int, stdin.readline().rstrip().split())) for i in range(N)]
time.sort(key=lambda t: t[1])
meeting = [time[0]]
for i in range(1, N):
    if is_collapsed(meeting[-1], time[i]):
        continue

    meeting.append(time[i])

print(len(meeting))
