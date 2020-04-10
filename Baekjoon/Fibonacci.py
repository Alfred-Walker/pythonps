# 입력: 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

# 출력: 첫째 줄에 n번째 피보나치 수를 출력한다.
# 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import sys


def get_fiv(memo, num):
    if num <= 1:
        return num
    else:
        a = 0
        b = 0
        if memo[num - 1] >= 0:
            a = memo[num - 1]
        else:
            a = get_fiv(memo, num - 1)
            memo[num - 1] = a

        if memo[num - 2] >= 0:
            b = memo[num - 2]
        else:
            b = get_fiv(memo, num - 2)
            memo[num - 2] = b

        return a + b


n = int(sys.stdin.readline().rstrip())
my_memo = [-1]*n
print(get_fiv(my_memo, n))
