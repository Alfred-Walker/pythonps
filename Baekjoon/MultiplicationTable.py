# 입력: 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력: 출력형식과 같게 N*1부터 N*9까지 출력한다.
N = int(input())
line = 9
for i in range(1, line+1):
    value = N * int(i)
    print(str(N) + " * " + str(i) + " = " + str(value))
