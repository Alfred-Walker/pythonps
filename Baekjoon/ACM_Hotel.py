# 프로그램은 표준 입력에서 입력 데이터를 받는다.
# 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다.
# 각 테스트 데이터는 한 행으로서
# H: 호텔의 층 수
# W: 각 층의 방 수
# N: 몇 번째 손님인지
# 를 나타낸다
# (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).

# 출력: 프로그램은 표준 출력에 출력한다.
# 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

import sys

T = int(sys.stdin.readline().rstrip())
H = [0] * T
W = [0] * T
N = [0] * T
for t in range(T):
    H[t], W[t], N[t] = map(int, sys.stdin.readline().rstrip().split())


def get_room_no(cnt_floor, max_width, guest_no):
    room = [0] * (max_width + 1) * (cnt_floor + 1)
    guest_floor = guest_no % cnt_floor
    if guest_floor == 0:
        guest_floor = cnt_floor
        room_no = int(guest_no / cnt_floor)
    else:
        room_no = int(guest_no / cnt_floor) + 1
    return guest_floor * 100 + room_no


for _ in range(T):
    print(get_room_no(H[_], W[_], N[_]))
