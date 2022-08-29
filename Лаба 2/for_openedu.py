class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class avl_tree(object):

	def __init__(self):
		self.root=None

	def insert_node(self, root, data):
		x = root
		y = None
		while x is not None:
			c = x.data - data
			if c == 0:
				return
			else:
				y = x
				if c < 0:
					x = x.right
				else:
					x = x.left
		new_node = Node(data)
		if y is None:
			root = new_node
		else:
			if c > 0:
				y.left = new_node
			else:
				y.right = new_node

	def height_AVL(self, node):
		if node is None:
			return 0
		return max(self.height_AVL(node.left), self.height_AVL(node.right)) + 1


	def balance(self, x):
		left_root = x.left
		right_root = x.right

		left_height = 0
		right_height = 0

		if left_root is not None:
			left_height = height(left_root)

		if right_root is not None:
			right_height = height(right_root)

		return right_height - left_height

	def cont_level_order(self, x):
		queue = [x]
		while len(queue) != 0:
			if len(queue) != 0:
				x = queue.pop()

			print(self.balance(x))

			if x.left is not None:
				queue.append(x.left)

			if x.right is not None:
				queue.append(x.right)

tree = avl_tree()
n = int(input())
nodes = [int(i) for i in input().split()]
for i in range(n):
	tree.insert_node(tree.root, nodes[i])
tree.cont_level_order(tree.root)


