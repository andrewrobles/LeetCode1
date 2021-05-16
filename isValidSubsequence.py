def isValidSubsequence(array, sequence):
    """
    Write a function that determines whether the
    second array is a subsequence of the first
    """
    arrayIndex = 0
    sequenceIndex = 0

    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1

    return sequenceIndex == len(sequence)