def minHeightBst(array):
    return constructBST(array, 0, len(array)-1)


def constructBST(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = BST(array[mid])

    bst = BST(array[mid])
    
    bst.left = constructBST(array, start, mid - 1)
    bst.right = constructBST(array, mid + 1, end)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
