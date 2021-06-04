def longestCommonPrefix(strs):
    prefix = ""

    for i in range(len(strs)):
        if len(strs[0]) == 0:
            return ""
            
        currChar = strs[0][i] 

        isMatch = True

        for currString in strs:
            if currString[i] != currChar:
                isMatch = False
        
        if isMatch:
            prefix += currChar
        else:
            break
    
    return prefix

            


