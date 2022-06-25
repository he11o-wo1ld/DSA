def invertBinaryTree(tree):
    # Write your code here.
    queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current is None:
			continue
		swap(current)
		queue.append(current.left)
		queue.append(current.right)

def swap(node):
	node.left, node.right = node.right, node.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
