def romanToInteger(s):
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    value = 0

    for i in range(len(s)):

        currDigit = s[i]
        sumVal = symbols[currDigit]

        if i < len(s) - 1:
            nextDigit = s[i + 1]
            if symbols[currDigit] < symbols[nextDigit]:
                sumVal *= -1

        value += sumVal
    return value