def isPalindromeLinkedList(head):
    slow = head
	fast = head
	
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		
	secondHalf = reverseLinks(slow)
	firstHalf = head
	
	while secondHalf:
		if secondHalf.value != firstHalf.value:
			return False
		
		secondHalf = secondHalf.next
		firstHalf = firstHalf.next
		
	return True

def reverseLinks(head):
	prev, curr = None, head
	
	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
		
	return prev