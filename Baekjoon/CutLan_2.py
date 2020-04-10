# 집에서 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
# 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
# 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
# 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다.(이미 자른 랜선은 붙일 수 없다.)
#
# 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
# 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자.
# 이 때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.


# 입력: 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. (K ≦ N)
# 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.
# 랜선의 길이는 2^31-1보다 작거나 같은 자연수이다.

# 출력: 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
import sys


K, N = map(int, sys.stdin.readline().rstrip().split())
cables = [int(sys.stdin.readline().rstrip()) for i in range(K)]
min_piece_length = 1
max_piece_length = max(cables)
target_piece_length = 0


def cnt_piece(unit_length, whole_cables):
    ret = 0
    for c in whole_cables:
        ret += c // unit_length

    return ret


while min_piece_length <= max_piece_length:
    mid = int((min_piece_length + max_piece_length) >> 1)

    piece_cnt = cnt_piece(mid, cables)

    # 문제의 "N개를 만들 수 있는" 은 "N개 이상을 만들 수 있는 경우"도 포함하므로 주의
    if piece_cnt >= N:
        target_piece_length = max(target_piece_length, mid)
        min_piece_length = mid + 1
    else:
        max_piece_length = mid - 1


print(target_piece_length)
