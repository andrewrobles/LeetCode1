def isMonotonic(array):
    return isNonInc(array) or isNonDec(array)

def isNonInc(array):
	for i in range(len(array)-1):
		if array[i+1] > array[i]:
			return False
	return True

def isNonDec(array):
	for i in range(len(array)-1):
		if array[i+1] < array[i]:
			return False
	return True