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

        if isSpecialCase(s, i):
            sumVal *= -1
            
        value += sumVal

    return value

def isSpecialCase(s, i):
    currDigit = s[i]

    # Out of bounds check
    if i < len(s) - 1:
        nextDigit = s[i + 1]

        # Check for special case: I
        if currDigit == 'I' and (nextDigit == 'V' or nextDigit == 'X'):
            return True
        
        # Check for special case: X
        if currDigit == 'X' and (nextDigit == 'L' or nextDigit=='C'):
            return True
        
        # Check for special case: C
        if currDigit == 'C' and (nextDigit == 'D' or nextDigit=='M'):
            return True 

    return False 
