# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
#
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다.
# +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
# -를 누르면 -1된 채널로 이동한다.
# 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
#
# 수빈이가 지금 이동하려고 하는 채널은 N이다.
# 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#
# 수빈이가 지금 보고 있는 채널은 100번이다.
#
# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
# 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
#
# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

# 이후 60ms 코드들 다시 읽어볼 것.

from sys import stdin
import sys

N = stdin.readline().rstrip()
int_N = int(N)
M = int(stdin.readline().rstrip())
if M != 0:
    BROKEN = stdin.readline().rstrip().split()
else:
    BROKEN = []
max_nonzero_usable_num = -1
min_nonzero_usable_num = sys.maxsize
for i in range(1, 10):
    if str(i) not in BROKEN:
        max_nonzero_usable_num = max(max_nonzero_usable_num, i)
        min_nonzero_usable_num = min(min_nonzero_usable_num, i)


def get_direct_move_cnt(num_string):
    for s in num_string:
        if s in BROKEN:
            return sys.maxsize      # 0을 리턴하는 것이 아님에 주의

    return len(num_string)


# 시작 채널에서 한채널씩 이동
answer = abs(100 - int_N)

# 1~9 버튼이 부서짐
if min_nonzero_usable_num == sys.maxsize:
    # 0이 부서지지 않은 경우 검사
    if '0' not in BROKEN:
        answer = min(answer, int_N + 1)
    print(answer)
else:
    # 번호를 눌러 가까운 곳까지 바로 이동
    # (실제로는 가까운 곳을 알 수 없으므로 모든 경우의 수를 체크)

    # 1. 가능한 전체 범위를 체크하는 방법
    # for i in range(10 * (len(N) - 1), 1000001):
    # 왜 1,000,000까지 체크하는가?
    # => 더 작은 수에서 접근하는 경우가 0~500,000이기 때문에.
    # (더 큰 수에서 접근하는 경우를 고려해서 두배 범위)

    # 2. 사용 가능한 버튼으로 범위를 추린 후 그 안에서 체크하는 방법
    # 사용 가능한 버튼으로 만들 수 있는 한자리 적은 수
    if len(N) != 1:
        # min_range = int(str(max_nonzero_usable_num) * (len(N) - 1))
        min_range = int(''.join([str(max_nonzero_usable_num) for _ in range(len(N) - 1)]))
    else:
        min_range = 0

    # 사용 가능한 버튼으로 만들 수 있는 한자리 많은 수
    # max_range = int(str(min_nonzero_usable_num) * (len(N) + 1))
    max_range = int(''.join([str(min_nonzero_usable_num) for _ in range(len(N) + 1)]))

    # N의 범위에 유의. 500,000보다 한자리 더 많다면 5,000,000이 되어버려서 범위가 지나치게 커짐
    # -100은 시작 지점.
    max_range = min(max_range, 1000000 - 100)

    # 반드시 max_range를 포함하여 검사할 것
    for i in range(min_range, max_range + 1):
        direct_move_cnt = get_direct_move_cnt(str(i))

        if direct_move_cnt != sys.maxsize:  # sys.maxsize 리턴하는 경우에 주의
            answer = min(answer, abs(int_N - i) + direct_move_cnt)

    print(answer)
