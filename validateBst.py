def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(node, minVal, maxVal):
	if not node:
		return True
	if not node.value >= minVal or not node.value < maxVal:
		return False
	
	leftIsValid = validateBstHelper(node.left, minVal, node.value)
	rightIsValid = validateBstHelper(node.right, node.value, maxVal)
	
	return leftIsValid and rightIsValid