# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    arr = []
	inOrderArray = InOrder(tree, arr)
	
	for idx, curr in enumerate(inOrderArray):
		if curr != node:
			continue
		
		if idx == len(inOrderArray) - 1:
			return None
		return inOrderArray[idx+1]


def InOrder(node, array):
	if node is None:
		return array
	if node.left is not None:
		InOrder(node.left, array)
	array.append(node)
	if node.right is not None:
		InOrder(node.right, array)
	return array
