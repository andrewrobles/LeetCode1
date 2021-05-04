def isPalindrome(head):
    vals = []
    currentNode = head

    while currentNode is not None:
        vals.append(currentNode.val)
        currentNode = currentNode.next
        
    return vals == vals[::-1]