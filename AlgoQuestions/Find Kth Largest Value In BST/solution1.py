# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
	nums = []
	inOrderTraverse(tree, nums)
	return nums[len(nums) - k]

def inOrderTraverse(node, nums):
	if node is None:
		return
	
	inOrderTraverse(node.left, nums)
	nums.append(node.value)
	inOrderTraverse(node.right, nums)
