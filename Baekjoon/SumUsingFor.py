# 입력: 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 출력: 1부터 n까지 합을 출력한다.
n = int(input())
sumOfNum = 0
for i in range(1, n+1):
    sumOfNum += i

print(sumOfNum)
