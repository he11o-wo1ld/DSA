# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, rootIdx):
		self.rootIdx = rootIdx
		
		
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
	return constructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)
	
def constructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	
	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	
	currentSubtreeInfo.rootIdx += 1
	leftSubtree = constructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
	rightSubtree = constructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
	return BST(rootValue, leftSubtree, rightSubtree)
