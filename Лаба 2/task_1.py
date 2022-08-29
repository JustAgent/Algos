class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = BinaryTreeNode(root_data)

    def __str__(self):
        preorder_recursive = str(self.preorder_dfs_recursive(self.root))
        inorder_recursive = str(self.inorder_dfs_recursive(self.root))
        postorder_recursive = str(self.postorder_dfs_recursive(self.root))

        return f"""
			\nPre-Order\n{preorder_recursive}
			\nIn-Order\n{inorder_recursive}
			\nPost-Order\n{postorder_recursive}
		"""

    def preorder_dfs_recursive(self, start_node, result=[]):
        if start_node is not None:
            result.append(start_node.data)
            self.preorder_dfs_recursive(start_node.left, result)
            self.preorder_dfs_recursive(start_node.right, result)
        return result

    def inorder_dfs_recursive(self, start_node, result=[]):
        if start_node is not None:
            self.inorder_dfs_recursive(start_node.left, result)
            result.append(start_node.data)
            self.inorder_dfs_recursive(start_node.right, result)
        return result

    def postorder_dfs_recursive(self, start_node, result=[]):
        if start_node is not None:
            self.postorder_dfs_recursive(start_node.left, result)
            self.postorder_dfs_recursive(start_node.right, result)
            result.append(start_node.data)
        return result


#          2
#        /   \
#       1     3

binary_tree = BinaryTree(2)

binary_tree.root.left = BinaryTreeNode(1)
binary_tree.root.right = BinaryTreeNode(3)

print(binary_tree)
