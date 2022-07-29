class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    node1 = linkedListOne
    node2 = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = node1.value if node1 is not None else 0
        valueTwo = node2.value if node2 is not None else 0

        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode

        carry = sumOfValues // 10
        node1 = node1.next if node1 is not None else None
        node2 = node2.next if node2 is not None else None

    return newLinkedListHeadPointer.next
