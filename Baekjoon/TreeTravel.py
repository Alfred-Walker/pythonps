# 이진 트리를 입력받아
# 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)
# 한 결과를 출력하는 프로그램을 작성하시오.
#
# https://www.acmicpc.net/problem/1991
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
# 자식 노드가 없는 경우에는 .으로 표현된다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
import sys


# skewed tree일 경우를 고려한다고 리스트(배열)를 최대 크기로 만들면 메모리 초과
# 아래의 힙 방식보다 따로 노드 클래스 생성하는 편이 나음
# tree_size = (2 ** 26) - 1
# tree = [0] * (tree_size + 1)
N = int(sys.stdin.readline().rstrip())
tree = dict()
tree[1] = "A"
for i in range(1, N + 1):
    node = sys.stdin.readline().rstrip().split()
    pi = {key for (key, val) in tree.items() if val == node[0]}.pop()

    li = pi << 1
    ri = li + 1

    if node[1] != '.':
        tree[li] = node[1]

    if node[2] != '.':
        tree[ri] = node[2]


# 전위 순회: root-left-right
def pre_order_traversal(index):
    if index not in tree.keys():
        return

    left = index << 1
    right = left + 1
    print(tree[index], end="")
    pre_order_traversal(left)
    pre_order_traversal(right)


# 중위 순회: left-root-right
def in_order_traversal(index):
    if index not in tree.keys():
        return

    left = index << 1
    right = left + 1
    in_order_traversal(left)
    print(tree[index], end="")
    in_order_traversal(right)


# 후위 순회: left-right-root
def post_order_traversal(index):
    if index not in tree.keys():
        return

    left = index << 1
    right = left + 1
    post_order_traversal(left)
    post_order_traversal(right)
    print(tree[index], end="")


pre_order_traversal(1)
print("\n", end="")
in_order_traversal(1)
print("\n", end="")
post_order_traversal(1)
