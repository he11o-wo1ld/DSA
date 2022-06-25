def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	swap(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	
def swap(node):
	node.left, node.right = node.right, node.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
