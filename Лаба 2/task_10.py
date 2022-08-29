import sys


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def check(self, root_node, min=-sys.maxsize, max=sys.maxsize):
        if root_node is not None:
            if root_node.data >= min and root_node.data <= max and self.check(root_node.left, min,
                                                                                     root_node.data) and self.check(
                    root_node.right, root_node.data, max):
                return "YES"
            else:
                return "NO"
        else:
            return "YES"


#          2
#        /    \
#       1     3
f1 = BinarySearchTree()
f1.root = BinarySearchTreeNode(2)
f1.root.left = BinarySearchTreeNode(1)
f1.root.right = BinarySearchTreeNode(3)

#          2
#        /    \
#       3     1
f2 = BinarySearchTree()
f2.root = BinarySearchTreeNode(2)
f2.root.left = BinarySearchTreeNode(3)
f2.root.right = BinarySearchTreeNode(1)

#TESTS
print(f1.check(f1.root))
print(f2.check(f2.root))
