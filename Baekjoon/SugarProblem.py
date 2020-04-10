# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 최대한 적은 봉지를 들고 가려고 한다. #
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지
# 그 수를 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
# 출력: 상근이가 배달하는 봉지의 최소 개수를 출력한다.
# 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
n = int(input())

packA = int(3)
packB = int(5)
numPackA = int(0)
numPackB = int(0)
rest = n

numPackB = n // packB

while numPackB >= 0:
    rest = n - packB * numPackB

    if rest % packA != 0:
        numPackB -= 1
        continue
    else:
        numPackA = rest // packA
        break

if numPackB < 0:
    print(-1)
else:
    print(numPackA + numPackB)
