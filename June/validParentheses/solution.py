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

        # If closed compare stack to current
        elif stack:
            stackBracket = stack.pop()
            if matches[stackBracket] != currBracket:
                return False
        
        else:
            # When closed bracket and empty stack
            return False

    # Empty stack 
    return not stack