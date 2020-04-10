# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
#
# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.
#
# 예제 입력 1
# 10
# 예제 출력 1
# 2

import sys


memo = dict()


def get_factor_cnt(num, factor):
    if (num, factor) in memo.keys():
        return memo[(num, factor)]

    temp = num
    ret = 0
    while temp % factor == 0:
        if (temp, factor) in memo.keys():
            ret += memo[(temp, factor)]
            break
        else:
            temp //= factor
            ret += 1

    memo[(num, factor)] = ret
    return ret


N = int(sys.stdin.readline().rstrip())
cnt_2, cnt_5 = 0, 0
# factorial = 1
for i in range(1, N + 1):
    # factorial *= i
    cnt_2 += get_factor_cnt(i, 2)
    cnt_5 += get_factor_cnt(i, 5)

# print(factorial)  확인용 코드
print(min(cnt_2, cnt_5))
