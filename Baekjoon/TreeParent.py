# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

import sys
sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline().rstrip())
connected = dict()
for n in range(1, N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a not in connected.keys():
        connected[a] = [b]
    else:
        connected[a].append(b)

    if b not in connected.keys():
        connected[b] = [a]
    else:
        connected[b].append(a)


def remove_except_parent(num, parent):
    for i in range(len(connected[num]) - 1, -1, -1):
        child = connected[num][i]
        if child != parent:
            connected[num].remove(child)
            remove_except_parent(child, num)


remove_except_parent(1, -1)
for i in range(2, N+1):
    print(connected[i][0])
