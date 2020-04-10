# 문제
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.
#
# 출력
# 첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.

import sys


def get_bin_from_oct(num):
    if num == 0:
        return "000"
    elif num == 1:
        return "001"
    elif num == 2:
        return "010"
    elif num == 3:
        return "011"
    elif num == 4:
        return "100"
    elif num == 5:
        return "101"
    elif num == 6:
        return "110"
    elif num == 7:
        return "111"


num_oct = sys.stdin.readline().rstrip()
answer = ""

# print(bin(int(num_oct, 8)))             # 0b11001100
# print(format(int(num_oct, 8), 'b'))     # 11001100 - format을 이용한 접두어 제외

if num_oct == '0':
    print(0)
    exit()

for o in num_oct:
    answer = answer + get_bin_from_oct(int(o))

print(answer.lstrip('0'))



'''
느린 방식
num_binary = ""
memo = dict()
if num_oct == '0':
    print(0)
    exit()

for i in range(len(num_oct) - 1, -1, -1):
    n = int(num_oct[i])

    if n in memo.keys():
        num_binary = memo[n] + num_binary
        continue

    memo[int(num_oct[i])] = ""

    if n == 0:
        num_binary = "000" + num_binary
    else:
        for j in range(0, 3):
            mod = n % 2
            n >>= 1
            memo[int(num_oct[i])] = str(mod) + memo[int(num_oct[i])]

    num_binary = memo[int(num_oct[i])] + num_binary

print(num_binary.lstrip('0'))
'''