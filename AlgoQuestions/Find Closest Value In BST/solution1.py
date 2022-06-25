def findClosestValueInBst(tree, target):
    # Write your code here.
	return findClosestValue(tree, target, float("inf"))

# def findClosestValue(tree, target, close):
# 	if tree is None:
# 		return close
# 	if abs(target - close) > abs(target - tree.value):
# 		close = tree.value
# 	if target < tree.value:
# 		return findClosestValue(tree.left, target, close)
# 	elif target > tree.value:
# 		return findClosestValue(tree.right, target, close)
# 	else:
# 		return close

def findClosestValue(tree, target, close):
	curr = tree
	while curr is not None:
		if abs(target - close) > abs(target - curr.value):
			close = curr.value
		if target < curr.value:
			curr = curr.left
		elif target > curr.value:
			curr = curr.right
		else:
			break
	return close

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
	
		
	