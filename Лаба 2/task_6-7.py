from typing import List
import sys


class TreeNode():
    root: int
    children: List[int]

    def __init__(self, root, left, right):
        self.root = root
        self.children = [left, right]


tree = []
_input = """3
2 1 2
1 -1 -1
2 -1 -1"""

_input = _input.split("\n")
n = int(_input[0])


def is_valid(tree, node, min_root, max_root):
    if node == -1:
        return True
    if tree[node].root <= min_root or tree[node].root >= max_root:
        return False

    result_left = is_valid(tree, tree[node].children[0], min_root, tree[node].root)
    result_right = is_valid(tree, tree[node].children[1], tree[node].root, max_root)

    return result_left and result_right


for line in _input[1:]:
    root, left, right = list(map(int, line.split(" ")))
    tree.append(TreeNode(root, left, right))

if n == 0:
    print("CORRECT")
else:
    if is_valid(tree, 0, -sys.maxsize - 1, sys.maxsize + 1):
        print("CORRECT")
    else:
        print("INCORRECT")
