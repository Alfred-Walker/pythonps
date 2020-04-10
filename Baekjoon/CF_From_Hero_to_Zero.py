import sys


T = int(sys.stdin.readline().rstrip())
for t in range(T):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    answer = 0

    while n > 0:
        r = n % k
        if r == 0:
            n //= k
            answer += 1
        else:
            n -= r
            answer += r

    print(answer)
