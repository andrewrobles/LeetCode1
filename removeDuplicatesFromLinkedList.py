def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
	
    while curr:
        next = curr.next
		
        while next and next.value == curr.value:
            next = next.next
		
        curr.next = next
        curr = next
	
    return linkedList