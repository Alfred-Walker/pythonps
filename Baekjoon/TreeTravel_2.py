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


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def map_alphabet_to_index(a):
    return ord(a) - ord('A')


N = int(sys.stdin.readline().rstrip())
tree = [None] * N
for i in range(1, N + 1):
    input_text = sys.stdin.readline().rstrip().split()
    pi = map_alphabet_to_index(input_text[0])
    li = map_alphabet_to_index(input_text[1])
    ri = map_alphabet_to_index(input_text[2])

    if tree[pi] is None:
        tree[pi] = Node(input_text[0])

    if input_text[1] != '.' and tree[li] is None:
        tree[li] = Node(input_text[1])
        tree[pi].left = tree[li]

    if input_text[2] != '.' and tree[ri] is None:
        tree[ri] = Node(input_text[2])
        tree[pi].right = tree[ri]


# root - left - right
def pre_order(start_node):
    answer = [start_node.key]

    if start_node.left is not None:
        answer += pre_order(start_node.left)

    if start_node.right is not None:
        answer += pre_order(start_node.right)

    return answer


# left - root - right
def in_order(start_node):
    answer = []

    if start_node.left is not None:
        answer += in_order(start_node.left)

    answer += start_node.key

    if start_node.right is not None:
        answer += in_order(start_node.right)

    return answer


# left - right - root
def post_order(start_node):
    answer = []

    if start_node.left is not None:
        answer += post_order(start_node.left)

    if start_node.right is not None:
        answer += post_order(start_node.right)

    answer += start_node.key

    return answer


print(*pre_order(tree[0]), sep="")
print(*in_order(tree[0]), sep="")
print(*post_order(tree[0]), sep="")
