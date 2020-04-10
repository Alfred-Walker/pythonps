import sys


T = int(sys.stdin.readline().rstrip())
for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip()
    exist_operation = False

    for i in range(0, len(nums) - 10):
        if nums[i] == '8':
            exist_operation = True
            break

    if exist_operation:
        print("YES")
    else:
        print("NO")
