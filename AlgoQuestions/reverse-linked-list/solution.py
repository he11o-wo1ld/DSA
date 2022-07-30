class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    if head == None and head.next == None:
        return head
    
    curr = head
    next = None
    prev = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
