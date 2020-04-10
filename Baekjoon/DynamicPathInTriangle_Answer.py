import sys
n = int(sys.stdin.readline())
max_path = [0]
for i in range(n):
    cur = list(map(int, sys.stdin.readline().strip().split()))
    new = [0]*len(cur)
    new[0] = max_path[0] + cur[0]
    for i in range(1,len(cur)-1):
        new[i] = max(max_path[i-1],max_path[i])+cur[i]
    if len(cur) > 1:
        new[-1] = max_path[-1]+cur[-1]
    max_path = new
print(max(max_path))
