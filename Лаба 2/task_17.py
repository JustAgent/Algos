import sys


class TreeNode:
    def __init__(self, key, sum, left, right, parent):
        self.key, self.sum, self.left, self.right, self.parent = \
            key, sum, left, right, parent


class SplayTree:
    @staticmethod
    def update(node):
        if node is None:
            return
        node.sum = node.key + (node.left.sum if node.left is not None else 0) + (
            node.right.sum if node.right is not None else 0)
        if node.left is not None:
            node.left.parent = node
        if node.right is not None:
            node.right.parent = node

    @classmethod
    def _small_rotation(cls, node):
        parent = node.parent
        if parent is None:
            return
        grandparent = node.parent.parent
        if parent.left == node:
            m = node.right
            node.right = parent
            parent.left = m
        else:
            m = node.left
            node.left = parent
            parent.right = m
        cls.update(parent)
        cls.update(node)
        node.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node

    @classmethod
    def _big_rotation(cls, node):
        if node.parent.left == node and node.parent.parent.left == node.parent:
            cls._small_rotation(node.parent)
            cls._small_rotation(node)
        elif node.parent.right == node and node.parent.parent.right == node.parent:
            cls._small_rotation(node.parent)
            cls._small_rotation(node)
        else:
            cls._small_rotation(node)
            cls._small_rotation(node)

    @classmethod
    def splay(cls, node):
        if node is None:
            return None
        while node.parent is not None:
            if node.parent.parent is None:
                cls._small_rotation(node)
                break
            cls._big_rotation(node)
        return node

    @classmethod
    def find(cls, root, key):
        node = root
        last = root
        next_ = None
        while node is not None:
            if node.key >= key and (next_ is None or node.key < next_.key):
                next_ = node
            last = node
            if node.key == key:
                break
            if node.key < key:
                node = node.right
            else:
                node = node.left
        root = cls.splay(last)
        return next_, root

    @classmethod
    def split(cls, root, key):
        result, root = SplayTree.find(root, key)
        if result is None:
            return root, None
        right = cls.splay(result)
        left = right.left
        right.left = None
        if left is not None:
            left.parent = None
        cls.update(left)
        cls.update(right)
        return left, right

    @classmethod
    def merge(cls, left, right):
        if left is None:
            return right
        if right is None:
            return left
        while right.left is not None:
            right = right.left
        right = cls.splay(right)
        right.left = left
        cls.update(right)
        return right


class Set:
    root = None

    def add(self, key):
        left, right = SplayTree.split(self.root, key)
        new_tree_node = None
        if right is None or right.key != key:
            new_tree_node = TreeNode(key, key, None, None, None)
        self.root = SplayTree.merge(SplayTree.merge(left, new_tree_node), right)

    def delete(self, key):
        if self.search(key) is None:
            return

        SplayTree.splay(self.root)
        self.root = SplayTree.merge(self.root.left, self.root.right)
        if self.root is not None:
            self.root.parent = None

    def search(self, key):
        result, self.root = SplayTree.find(self.root, key)
        if result is None or result.key != key:
            return None
        return result.key

    def sum(self, fr, to):
        left, middle = SplayTree.split(self.root, fr)
        middle, right = SplayTree.split(middle, to + 1)

        if middle is None:
            result = 0
            self.root = SplayTree.merge(left, right)
        else:
            result = middle.sum
            self.root = SplayTree.merge(SplayTree.merge(left, middle), right)

        return result


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    last_sum_result = 0
    const = 1000000001

    s = Set()
    for i in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "+":
            x = int(line[1])
            s.add((x + last_sum_result) % const)
        elif line[0] == "-":
            x = int(line[1])
            s.delete((x + last_sum_result) % const)
        elif line[0] == "?":
            x = int(line[1])
            print(
                "Found" if s.search(
                    (x + last_sum_result) % const) is not None else "Not found"
            )
        elif line[0] == "s":
            l = int(line[1])
            r = int(line[2])
            res = s.sum((l + last_sum_result) % const,
                        (r + last_sum_result) % const)
            print(res)
            last_sum_result = res % const