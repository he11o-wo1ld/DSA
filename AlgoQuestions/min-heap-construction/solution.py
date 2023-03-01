class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        self.heap = []
        for a in array:
            self.insert(a)
        return self.heap

    def siftDown(self, index):
        # Write your code here.
        smallest = index
        if self.hasLeftChild(index) and self.heap[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.heap[smallest] > self.rightChild(index):
            smallest = self.getRightChildIndex(index)
        if smallest != index:
            self.swap(index, smallest)
            self.siftDown(smallest)

    def siftUp(self, index):
        # Write your code here.
        if self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.getParentIndex(index), index)
            self.siftUp(self.getParentIndex(index))

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        data = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.siftDown(0)
        return data
    
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return (2 * index) + 1

    def getRightChildIndex(self, index):
        return (2 * index) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.heap)

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.heap)

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]





    
