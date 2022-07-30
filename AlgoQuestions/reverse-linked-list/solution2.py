class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    if head == None or head.next == None:
        return head

    curr = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return curr
