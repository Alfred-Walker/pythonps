from itertools import combinations
from sys import stdin

while True:
    lis = list(map(int, stdin.readline().rstrip().split()))[1:]
    if len(lis) == 0:
        break

    for c in combinations(lis, 6):
        print(*c)

    print()
