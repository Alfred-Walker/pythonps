import sys


def get_triangle(n, last_drawn):
    ret = []
    last_drawn = last_drawn.split("\n")         # 이미 그려진 삼각형

    for i in range(n//2):
        ret.append(' ' * (n//2) + last_drawn[i] + ' ' * (n//2)) # 이미 그려진 삼각형 밑에 n//2만큼 추가될 것이므로 각각 공백을 양끝에 n//2칸씩 추가

    for i in range(n//2):
        ret.append(last_drawn[i] + ' ' + last_drawn[i])         # 좌우 공백을 포함한 문자열을 빈칸을 사이에 둬서 합침

    return "\n".join(ret)


N = int(sys.stdin.readline().rstrip())
drawn = "  *  \n * * \n*****"

if N == 3:
    print(drawn)
else:
    for i in range(1, 11):
        drawn = get_triangle(3 * (2 ** i), drawn)
        if 3 * (2 ** i) == N:
            break

    print(drawn)
