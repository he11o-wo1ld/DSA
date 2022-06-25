# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
	while head is not None:
		curr = head.next
		while curr is not None and curr.value == head.value:
			curr = curr.next
		
		head.next = curr
		head = curr
	return linkedList
