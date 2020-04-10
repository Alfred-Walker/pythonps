# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
# 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 n(1≤n≤100,000)이 주어진다.
# 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고,
# 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

# 출력: 첫째 줄에 프리오더를 출력한다.

import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline().rstrip())
in_order = sys.stdin.readline().rstrip().split()    # left-root-right
post_order = sys.stdin.readline().rstrip().split()  # left-right-root

position = {}
for i in range(n):
    position[in_order[i]] = i


def print_pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    root_index = position[root]

    print(root, end=' ')
    print_pre_order(
                    in_start, root_index - 1,
                    post_start, post_start + (root_index - in_start - 1))

    print_pre_order(
                    root_index + 1, in_end,
                    post_start + (root_index - in_start), post_end - 1)


print_pre_order(0, n - 1, 0, n - 1)
