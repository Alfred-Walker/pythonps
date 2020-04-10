# 입력: 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 출력: 1부터 n까지 합을 출력한다.
n = int(input())
nums = input()
sumOfNum = 0

for i in nums:
    sumOfNum += int(i)

print(sumOfNum)
