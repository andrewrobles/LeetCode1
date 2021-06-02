def twoNumberSum(array, targetSum):
	nums = set()
	
	for curr in array:
		potentialMatch = targetSum - curr
		
		if potentialMatch in nums:
			return [potentialMatch, curr]
		else:
			nums.add(curr)
			
	return []