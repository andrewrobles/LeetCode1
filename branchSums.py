def branchSums(root):
	array = []
	calcBranchSums(root, 0, array)
	return array

def calcBranchSums(node, currentSum, array):	
	if node is None:
		return
	
	currentSum = currentSum + node.value
	
	if node.left is None and node.right is None:
		array.append(currentSum)
	
	calcBranchSums(node.left, currentSum, array)	
	calcBranchSums(node.right, currentSum, array)