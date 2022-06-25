# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return construct(preOrderTraversalValues, None)

def construct(nums, node):
	index = 0
	current = nums[0]
	while index < len(nums):
		if node is None:
			node = current
			index += 1
		else:
			if current < node:
				node.left = current
				node = node.left
			else:
				node.right = current
				node = node.right
			index += 1
		
