class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def height(self):
        if self.root is not None:
            return self.root.height
        else:
            return 0

    def insert(self, data):
        new_node = Node(data)

        if self.root is not None:
            if data < self.root.data:
                self.root.left.insert(data)
            elif data > self.root.data:
                self.root.right.insert(data)
            else:
                print("Node is already in AVL")
                return
        else:
            self.root = new_node
            self.root.left = AVLTree()
            self.root.right = AVLTree()

        self.rebalance()

    def rebalance(self):

        self.count_new_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:

            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.rotate_left()
                    self.count_new_heights()
                    self.update_balances()
                self.rotate_right()
                self.count_new_heights()
                self.update_balances()

            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.rotate_right()
                    self.count_new_heights()
                    self.update_balances()
                self.rotate_left()
                self.count_new_heights()
                self.update_balances()

    def rotate_right(self):
        print("Rotating ", self.root.data, " right")

        a = self.root
        b = self.root.left.root
        c = b.right.root

        self.root = b
        b.right.root = a
        a.left.root = c

    def rotate_left(self):
        print("Rotating ", self.root.data, " left")

        a = self.root
        b = self.root.right.root
        c = b.left.root

        self.root = b
        b.left.root = a
        a.right.root = c

    def count_new_heights(self, recurse=True):
        if not self.root is None:
            if recurse:
                if self.root.left is not None:
                    self.root.left.count_new_heights()
                if self.root.right is not None:
                    self.root.right.count_new_heights()

            self.height = max(self.root.left.height, self.root.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.root is None:
            if recurse:
                if self.root.left is not None:
                    self.root.left.update_balances()
                if self.root.right is not None:
                    self.root.right.update_balances()

            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0

    def delete(self, data):

        if self.root is not None:
            if self.root.data == data:
                print("Deleting node: ", data)

                if self.root.left.root is None and self.root.right.root is None:
                    self.root = None
                elif self.root.left.root is None and self.root.right.root is not None:
                    self.root = self.root.right.root
                elif self.root.left.root is not None and self.root.right.root is None:
                    self.root = self.root.left.root
                else:
                    replacement = self.next(self.root)
                    if replacement is not None:
                        self.root.data = replacement.data
                        self.root.right.delete(replacement.data)

                self.rebalance()
                return
            elif data < self.root.data:
                self.root.left.delete(data)
            elif data > self.root.data:
                self.root.right.delete(data)

            self.rebalance()
        else:
            return

    def prev(self, root):
        root = root.left.root

        if root is not None:
            while root.right is not None:
                if root.right.root is None:
                    return root
                else:
                    root = root.right.root

        return root

    def next(self, root):

        root = root.right.root

        if root is not None:
            while root.left is not None:
                if root.left.root is None:
                    return root
                else:
                    root = root.left.root

        return root.data

    def check_balanced(self):
        if self is None or self.root is None:
            return True

        self.count_new_heights()
        self.update_balances()

        return (abs(self.balance) < 2) and self.root.left.check_balanced() and self.root.right.check_balanced()

    def in_order(self):
        if self.root == None:
            return []

        visited = []

        left = self.root.left.in_order()
        for node in left:
            visited.append(node)

        visited.append(self.root.data)

        right = self.root.right.in_order()
        for node in right:
            visited.append(node)

        return visited


if __name__ == "__main__":
    tree = AVLTree()

    print("Insert")
    for i in [8, 4, 2, 6, 3, 5, 1, 7, 9, 1, 0, 11, 2, 13]:
        tree.insert(i)

    print(tree.in_order())

    print("Delete")
    tree.delete(3)
    tree.delete(4)
    tree.delete(5)
    print(tree.in_order())
    print(tree.root.right.height)
