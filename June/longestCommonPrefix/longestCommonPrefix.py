def longestCommonPrefix(strings):
    prefix = ""

    for i in range(len(strings)):
        currChar = strings[0][i]

        isMatch = True

        for currString in strings:
            if currString[i] != currChar:
                isMatch = False
        
        if isMatch:
            prefix += currChar
        else:
            break
    
    return prefix

            


