def threeNumberSum(array, targetSum):
    triplets = []
	array.sort()

    for curr in range(len(array)-2):
		left, right = curr + 1, len(array) - 1
		
		while left < right:
			total = array[curr] + array[left] + array[right]
			
			if total < targetSum:
				left += 1
                
			elif total > targetSum:
				right -= 1

			else:
				triplets.append([array[curr], array[left], array[right]])
				left += 1
				right -= 1

	return triplets