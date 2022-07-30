class LinkedList:
	def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
	first = head.next
	second = head.next.next

	while first != second:
		first = head.next
		second = head.next.next

	first = head
	while first != second:
		first = head.next
		second = head.next

	return second

