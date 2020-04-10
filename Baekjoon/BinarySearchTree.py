import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root is not None

    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        elif data <= node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    def find(self, key):
        return self._find(self.root, key) is not None

    def _find(self, node, key):
        if node is not None:
            if node.data == key:
                return True

            if key < node.data:
                return self._find(node.left, key)
            else:
                return self._find(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        if node is None:
            return node, False

        deleted = False

        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent = node
                child = node.right

                while child.left is not None:
                    parent = child
                    child = child.left

                # parent==node의 경우,child(node.right)가 우측에서 올라와 새로운 node가 될 뿐이므로
                # parent의 왼쪽 자식들에 대해 새로운 변경사항이 발생하지 않는다.
                # 따라서 아래의 조건문을 삭제할 수 없다.
                if parent != node:
                    # 지우려는 node의 우측에서 가장 작은 수가 child(left가 none인 노드)이고,
                    # 그 child가 지우려는 node 위치로 올라가므로 child의 parent는 left값을 새로 갱신해야한다.
                    # 이 때 child의 right는 항상 parent보다 작으므로 child의 right를 parent의 left로 설정한다.
                    # 또한 새로운 위치로 옮겨진 child는 새로운 right(지워질 node의 right)를 갖게 된다.
                    parent.left = child.right
                    child.right = node.right

                child.left = node.left  # 새로운 위치로 옮겨진 child는 새로운 left(지워질 node의 left)를 갖게 된다.
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete(node.left, key)
        else:
            node.right, deleted = self._delete(node.right, key)

        return node, deleted


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
