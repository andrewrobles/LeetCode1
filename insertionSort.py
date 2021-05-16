def insertionSort(array):
	"""
	Write a function that returns an array 
	that was sorted using insertion sort
	"""
    for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j - 1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]