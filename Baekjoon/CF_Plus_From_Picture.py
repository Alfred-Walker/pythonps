# https://codeforces.com/contest/1182/problem/B
import sys


H, W = map(int, sys.stdin.readline().rstrip().split())
picture = [sys.stdin.readline().rstrip() for h in range(H)]
answer = "YES"

if W < 3 or H < 3:
    print("NO")
else:
    is_cross = dict()

    dx = [-1, 0, 1, 0]
    dy = [1, 1, 1, 2]

    def check_cross(row, col):
        r = row
        c = col

        for i in range(4):
            if picture[r + dy[i]][col + dx[i]] != '*':
                return False

        while r < H and picture[r][col] == '*':
            is_cross[(r, col)] = True
            r += 1

        r = row

        while r >= 0 and picture[r][col] == '*':
            is_cross[(r, col)] = True
            r -= 1

        row += 1

        while c < W and picture[row][c] == '*':
            is_cross[(row, c)] = True
            c += 1

        c = col

        while c >= 0 and picture[row][c] == '*':
            is_cross[(row, c)] = True
            c -= 1

        return True


    def check_whole():
        global answer
        for hh in range(H):
            for ww in range(W):
                if picture[hh][ww] == '*' and (hh, ww) not in is_cross.keys():
                    answer = "NO"
                    return

                elif picture[hh][ww] == '.' and (hh, ww) in is_cross.keys():
                    answer = "NO"
                    return


    for h in range(0, H - 2):
        for w in range(1, W - 1):
            if picture[h][w] == '*':
                if check_cross(h, w):
                    check_whole()
                    print(answer)
                    exit(0)

    answer = "NO"
    print(answer)
