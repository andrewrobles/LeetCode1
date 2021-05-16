def productSum(array, multiplier=1):
	"""
	Write a function that takes in a "special"
	array and returns its product sum.
	"""
    sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier + 1)
		else:
			sum += element
	return sum * multiplier