def longestCommonPrefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        if len(strs[0]) == 0:
            return prefix

        currChar = strs[0][i] 

        isMatch = True

        for currString in strs:
            if i >= len(currString) or currString[i] != currChar:
                isMatch = False
        
        if isMatch:
            prefix += currChar
        else:
            break
    
    return prefix

            


