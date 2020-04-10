# 상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.
#
# 어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다.
# 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면, 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.
#
# 이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다.
# 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고, 가장 오른쪽 아래 칸에서 도착할 것이다.
# 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다.
# 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.
#
# 각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다.
# 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다.
# 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 R과 C가 주어진다. (2 ≤ R, C ≤ 1000)
# 둘째 줄부터 R개 줄에는 각 칸을 지나갈 때 얻을 수 있는 기쁨이 주어진다.
# 이 값은 1000보다 작은 양의 정수이다.
#
# 출력
# 첫째 줄에 가장 가장 큰 기쁨을 주는 롤러코스터는 가장 왼쪽 위 칸부터 가장 오른쪽 아래 칸으로
# 어떻게 움직이면 되는지를 출력한다.
# 위는 U, 오른쪽은 R, 왼쪽은 L, 아래는 D로 출력한다.
# 정답은 여러 가지 일 수도 있다.
#
from sys import stdin


R, C = map(int, stdin.readline().rstrip().split())
JOY = [[0]*C] + [[0] + list(map(int, stdin.readline().rstrip().split())) for r in range(R)]
path = ""
# 한 점을 들릴 수 없음.
# (체스판에 비유할 때, 시작과 끝이 흰색이라면 검은색 한칸을 못들림)
if R % 2 == 0 and C % 2 == 0:
    min_joy = 1000      # 문제에서 주어진 최대값
    min_joy_coord = (0, 0)
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if (r % 2 == 0 and c % 2 == 1) or (r % 2 == 1 and c % 2 == 0):
                if min_joy > JOY[r][c]:
                    min_joy = JOY[r][c]
                    min_joy_coord = (r, c)

    # new_r이 짝수 => 들리지 않는 점의 윗줄에서 좌측 끝
    if min_joy_coord[0] % 2 == 0:
        new_r = min_joy_coord[0] - 1
    # new_r이 홀수 => 들리지 않는 점이 있는 줄에서 좌측 끝
    else:
        new_r = min_joy_coord[0]

    # new_r인 줄(new_r이 홀수번째 줄), 혹은 new_r인 줄(new_r이 짝수번째 줄)의 바로 전 줄까지 이동
    for r in range(1, new_r):
        for c in range(2, C + 1):
            if r % 2 == 1:
                path += "R"
            else:
                path += "L"

        path += "D"

    # 들리지 않을 지점 바로 전의 열까지 이동
    for c in range(1, min_joy_coord[1]):
        if c % 2 == 1:
            path += "DR"    # 현재 지점이 홀수 c일 때, "다음 열"의 검은 칸은 위이므로 피해서 이동
        else:
            path += "UR"    # 현재 지점이 홀수 c일 때, "다음 열"의 검은 칸은 위쪽이므로 피해서 이동
    # 들리지 않을 지점 밑(혹은 위)부터 이동
    # 우측=>(위 또는 아래)로 움직이므로 C-1칸 까지 루프
    for c in range(min_joy_coord[1], C):
        if c % 2 == 1:
            path += "RD"    # 들리지 않을 지점(현재 지점의 밑이나 위)이 홀수 c일 때, 검은 칸은 아래쪽이므로 피해서 이동
        else:
            path += "RU"    # 들리지 않을 지점(현재 지점의 밑이나 위)이 짝수 c일 때, 검은 칸은 위쪽이므로 피해서 이동

    # 나머지 줄들에 대한 처리
    if min_joy_coord[0] % 2 == 1:
        left_line = min_joy_coord[0] + 2       # 방문하지 않는 점의 다다음줄부터
    else:
        left_line = min_joy_coord[0] + 1       # 방문하지 않는 점의 다음줄부터
    for r in range(left_line, R + 1):
        path += "D"
        for c in range(1, C):   # C - 1칸 이동하는 것에 주의
            if r % 2 == 1:
                path += "L"
            else:
                path += "R"


# (홀수행, 짝수열), (홀수행, 홀수열)
elif R % 2 == 1:
    for r in range(1, R + 1):
        for c in range(1, C):   # C - 1칸 움직이는 것에 주의 (시작 지점 고려)
            if r % 2 == 1:
                path += "R"
            else:
                path += "L"

        if r != R:
            path += "D"     # 마지막칸에 주의 (더 움직일 필요 없음)
# 짝수행, 홀수열
elif C % 2 == 1:
    for c in range(1, C + 1):
        for r in range(1, R):   # R - 1칸 움직이는 것에 주의 (시작 지점 고려)
            if c % 2 == 1:
                path += "D"
            else:
                path += "U"

        if c != C:              # 마지막칸에 주의 (더 움직일 필요 없음)
            path += "R"


print(path)
