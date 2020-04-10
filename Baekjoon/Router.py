# 도현이의 집 N개가 수직선 위에 있다.
# 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
#
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
#
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (1 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.


import sys


# C개의 공유기, N개의 집
# "가장 인접한" 두 공유기 사이의 거리(D)를 최대로
# => N개의 정렬된 집 위치들에 대해서 Gap 간격으로 최대한 배치했을 때
#    C개의 공유기가 설치되는 경우의 Gap 값을 저장
#    "가장 인접한" 두 공유기 사이의 거리가 중요하므로 Gap 보다 좀 더 먼 거리로 공유기 설치되는 경우는 신경 안써도 무방.
#    (Gap "이상"의 거리로 공유기가 설치되는 경우 세는게 중요)
N, C = map(int, sys.stdin.readline().rstrip().split())
coord = [int(sys.stdin.readline().rstrip()) for x in range(N)]
coord.sort()
d = (coord[-1] - coord[0]) // (C - 2)        # 양끝 집 사이의 거리를 C개의 공유기로 C - 2등분
answer = 1

start_gap = 1
end_gap = d

while start_gap <= end_gap:
    mid_gap = int((start_gap + end_gap) >> 1)
    cnt = 1     # 시작 지점. (coord[0])
    si = 0      # (정렬된) 첫번째 집

    for i in range(1, N):
        if coord[i] - coord[si] >= mid_gap:
            cnt += 1
            si = i

        if cnt > C:
            break

    # 현재 간격(mid_gap)으로 설치할 경우, 공유기 C개 이상 설치 가능
    # => 간격 더 늘려서 다른 경우도 확인.
    if cnt >= C:
        answer = max(answer, mid_gap)
        start_gap = mid_gap + 1
    # 현재 간격(mid_gap)으로 설치할 경우, 공유기 C개 이상 설치 불가능
    # => 간격 줄여야.
    else:
        end_gap = mid_gap - 1

print(answer)
