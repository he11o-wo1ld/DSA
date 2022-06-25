# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		

class TreeInfo:
    def __init__(self, numberOfNodeVisited, LatestVisitedNodeValue):
        self.numberOfNodeVisited = numberOfNodeVisited
        self.latestVisitedNodeValue = LatestVisitedNodeValue


def findKthLargestValueInBst(tree, k):
    treeinfo = TreeInfo(0, -1)
    reverseInorderTraverse(tree, k, treeinfo)
    return treeinfo.latestVisitedNodeValue


def reverseInorderTraverse(node, k, treeinfo):
    if node == None or treeinfo.numberOfNodeVisited >= k:
        return
    reverseInorderTraverse(node.right, k, treeinfo)
    if treeinfo.numberOfNodeVisited < k:
        treeinfo.numberOfNodeVisited += 1
        treeinfo.latestVisitedNodeValue = node.value
        reverseInorderTraverse(node.left, k, treeinfo)
