# 세준이는 N*N 크기의 배열을 만들었다. (배열의 방 번호는 1부터 시작한다.)
# 그 배열을 A라고 했을 때, 배열에 들어가는 수는 A[i][j] = i*j 이다.
# 세준이는 이 수를 일차원 배열 B에 넣으려고 한다. 그렇게 되면, B의 크기는 N*N이 될 것이다.
# 그러고 난 후에, B를 오름차순 정렬해서 k번째 원소를 구하려고 한다.
# N이 주어졌을 때, k번째 원소를 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 배열의 크기 N이 주어진다.
# N은 10^5보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(10^9, n^2)보다 작거나 같은 자연수이다.
# 출력: k번째 원소를 출력한다.

import sys


N = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

start = 1
end = k
ans = 0

while start <= end:
    cnt = 0
    mid = start + int((end - start) >> 1)
    for i in range(1, N + 1):
        cnt += min(int(mid / i), N)

    if cnt >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
