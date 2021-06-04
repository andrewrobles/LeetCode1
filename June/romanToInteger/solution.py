def romanToInteger(s):
    '''
    Read from left to right and add numbers as necessary.

    If special case is found then subtract that number
    ''' 
    value = 0 

    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for i in range(len(s)):

        currDigit = s[i]

        sumVal = symbols[currDigit]

        # Out of bounds check
        if i < len(s) - 1:
            nextDigit = s[i + 1]

            # Subtract sum value if special case
            if symbols[currDigit] < symbols[nextDigit]:
                sumVal *= -1

        value += sumVal

    return value