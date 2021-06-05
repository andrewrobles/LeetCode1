def solution(s):
    stack = []
    matches = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for currBracket in s:

        # If open add to stack
        if currBracket in matches:
            stack.append(currBracket)

        else:
            # Compare stack braket to currrent
            stackBracket = stack.pop()
            if matches[stackBracket] != currBracket:
                return False
    
    return True





