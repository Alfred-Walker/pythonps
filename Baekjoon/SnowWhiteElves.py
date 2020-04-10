# 입력: 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
# 출력: 키의 합이 100인 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
import sys

heights = [int(sys.stdin.readline().rstrip()) for i in range(0, 9)]
heights.sort()
diff = sum(heights) - 100

for i in range(0, 9):
    for j in range(i + 1, 9):
        if heights[i] + heights[j] == diff:
            del (heights[j])
            del (heights[i])
            print(*heights, sep="\n")
            exit(0)

