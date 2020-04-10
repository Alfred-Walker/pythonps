# 입력: 첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다.
# N 은 언제나 2의 제곱수로 주어지며, 1≤N ≤64의 범위를 가진다.
# 두 번째 줄부터는 길이 N 의 문자열이 N 개 들어온다.
# 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
# 출력: 영상을 압축한 결과를 출력한다.

# 5:42
import sys


N = int(sys.stdin.readline().rstrip())
video_data = [sys.stdin.readline().rstrip() for n in range(N)]


def get_compressed(r, c, size):
    if size == 1:
        return video_data[r][c]

    in_parenthesis = ""

    size = int(size >> 1)
    in_parenthesis += get_compressed(r, c, size)
    in_parenthesis += get_compressed(r, c + size, size)
    in_parenthesis += get_compressed(r + size, c, size)
    in_parenthesis += get_compressed(r + size, c + size, size)

    if in_parenthesis == '1111' or in_parenthesis == '0000':
        in_parenthesis = in_parenthesis[0]
        return in_parenthesis
    else:
        return "({0})".format(in_parenthesis)


result = get_compressed(0, 0, N)
print(result)
