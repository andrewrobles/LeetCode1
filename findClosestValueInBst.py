def findClosestValueInBst(tree, target):
    curr = tree
	closest = float('inf')
	
	while curr != None:
		
		if abs(target - curr.value) < abs(target - closest):
			closest = curr.value
			
		if curr.value < target:
			curr = curr.right
		else:
			curr = curr.left
		
	return closest