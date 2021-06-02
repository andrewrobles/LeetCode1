class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev, curr = None, head
	
	while curr is not None:
		next, curr.next = curr.next, prev
		prev, curr = curr, next
		
	return prev