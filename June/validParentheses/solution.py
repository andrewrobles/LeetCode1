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
            # Compare stack bracket to current
            stackBracket = stack.pop()
            if matches[stackBracket] != currBracket:
                return False

    # Empty stack 
    return not stack