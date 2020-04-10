# 문제
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
#
# 출력
# 첫째 줄에 0의 개수를 출력한다.
#
# 예제 입력 1
# 25 12
# 예제 출력 1
# 2

import sys

# 일반적인 factorial 계산 후 뒤부터 '0' 카운팅 => 시간 초과
# 소인수 분해 => 시간 초과
# memoization => 메모리 부족
# n 이하의 2, 2^2, 2^3..의 개수, 5, 5^2, 5^3..의 개수를 구해서 소인수 분해보다 빨리 2와 5의 개수를 구함
# (n/2 = n이하의 2의 배수, n/2^2 = n이하의 4의 배수...)

import sys


def get_factor_cnt(num, factor):
    ret = 0
    temp = factor
    while num >= temp:
        ret += num // temp
        temp *= factor

    return ret


n, m = map(int, sys.stdin.readline().rstrip().split())

n_cnt_2 = get_factor_cnt(n, 2)
n_cnt_5 = get_factor_cnt(n, 5)

m_cnt_2 = get_factor_cnt(m, 2)   # 나눗셈이기 때문에 뺄셈 적용
m_cnt_5 = get_factor_cnt(m, 5)   # 나눗셈이기 때문에 뺄셈 적용

n_m_cnt_2 = get_factor_cnt(n - m, 2)   # 나눗셈이기 때문에 뺄셈 적용
n_m_cnt_5 = get_factor_cnt(n - m, 5)   # 나눗셈이기 때문에 뺄셈 적용


print(max(0, min(n_cnt_2 - m_cnt_2 - n_m_cnt_2, n_cnt_5 - m_cnt_5 - n_m_cnt_5)))    # 2와 5가 최저 1개씩 있어야 0 1개
