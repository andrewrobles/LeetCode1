def palindromeNumber(x):
    '''Reverse the number and compare it original'''

    xRef, xFlipped = x, 0

    while xRef > 0:
        # Left shift flipped
        xFlipped *= 10

        # Add ones place to flipped
        xFlipped += xRef % 10

        # Right shift reference 
        xRef //= 10

    # Compare flipped to original
    return x == xFlipped