# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
N = int(input())
space = " "
star = "*"

for i in reversed(range(1, N+1)):
    print(space * (N-i) + star * i)
