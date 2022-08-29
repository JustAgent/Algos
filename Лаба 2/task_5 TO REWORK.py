import sys


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, data):

        if self.root is not None:
            return self._add(data, self.root)
        else:
            self.root = BinarySearchTreeNode(data)

    def _add(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is not None:
                self._add(data, cur_node.left)
            else:
                cur_node.left = BinarySearchTreeNode(data)
                cur_node.left.parent = cur_node
        elif data > cur_node.data:
            if cur_node.right is not None:
                self._add(data, cur_node.right)
            else:
                cur_node.right = BinarySearchTreeNode(data)
                cur_node.right.parent = cur_node
        else:
            print("Data already in tree !")

    def print_tree(self):
        print(str(self._print_tree(self.root)))

    def _print_tree(self, cur_node, result=[]):
        if cur_node is not None:
            self._print_tree(cur_node.left, result)
            result.append(cur_node.data)
            self._print_tree(cur_node.right, result)
        return result

    def print_len(self):
        if self.root is not None:
            print(self._print_len(self.root, 0))
        else:
            print(0)

    def _print_len(self, cur_node, cur_height):
        if cur_node is not None:
            left_height = self._print_len(cur_node.left, cur_height + 1)
            right_height = self._print_len(cur_node.right, cur_height + 1)
            return max(left_height, right_height)
        else:
            return cur_height

    def search(self, data):
        if self.root is not None:
            print(self._search(self.root, data))
        else:
            print(False)

    def _search(self, cur_node, data):

        if data == cur_node.data:
            return True

        elif data < cur_node.data and cur_node.left is not None:
            return self._search(cur_node.left, data)

        elif data > cur_node.data and cur_node.right is not None:
            return self._search(cur_node.right, data)

        return False

    def find(self, data):
        if self.root is not None:
            return self._find(self, cur_node, data)
        else:
            return None

    def _find(self, cur_node, data):
        if data == cur_node.data:
            return cur_node
        elif data < cur_node.data and cur_node.left is not None:
            return self._find(cur_node.left, data)
        elif data > cur_node.data and cur_node.right is not None:
            return self._find(cur_node.right, data)

    def get_min(self):
        cur_node = self.root
        while cur_node.left is not None:
            cur_node = cur_node.left
        print(cur_node.data)

    def get_max(self):
        cur_node = self.root
        while cur_node.right is not None:
            cur_node = cur_node.right
        print(cur_node.data)

    def delete_data(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):

        def number_of_children(node):
            number_of_children = 0
            if node.left is not None:
                number_of_children += 1
            elif node.right is not None:
                number_of_children += 1
            return number_of_children

        node_parent = node.parent
        node_children = number_of_children(node)

        if node_children == 0:

            if node_parent.parent is not None:

                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

            else:
                self.root = None

        if node_children == 1:

            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:

                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child

            else:
                self.root = child

            child.parent = node_parent

        if node_children == 2:

            def get_successor(node):
                cur_node = node
                while cur_node.left is not None:
                    cur_node = cur_node.left
                return cur_node

            successor = get_successor(node.right)
            node.data = successor.data
            self.delete_node(successor)

    def validate_bst(self, root_node, min=-sys.maxsize, max=sys.maxsize):
        if root_node is not None:
            if root_node.data >= min and root_node.data <= max and self.validate_bst(root_node.left, min,
                                                                                     root_node.data) and self.validate_bst(
                root_node.right, root_node.data, max):
                return True
            else:
                return False
        else:
            return True


binary_tree = BinarySearchTree()

binary_tree.add(10)
binary_tree.add(5)
binary_tree.add(15)

#          10
#        /    \
#       5     15

binary_tree.print_tree()
binary_tree.print_len()
binary_tree.search(15)
binary_tree.search(9)
binary_tree.get_min()
binary_tree.get_max()
print(binary_tree.validate_bst(binary_tree.root))
