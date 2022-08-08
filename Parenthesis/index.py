def isValid(s):
    stack = []
    hashVal = {
        # '(': ')',
        ')': '(',
        # '[': ']',
        ']': '[',
        # '{': '}',
        '}': '{'
    }
    for i, a in enumerate(s):
        stack.append(s[i])
        # print(">>>", stack)
        if i == 0:
            continue
        if len(stack) >= 2:
            # print(hashVal[stack[-1]], stack[-2])
            while len(stack) >= 2 and stack[-1] in hashVal and hashVal[stack[-1]] == stack[-2]:
                stack.pop(-1)
                # print("Stack", stack)
                stack.pop(-1)
                # print("Stack", stack)
    # print(">>len",stack)
    if len(stack) == 0:
        return True
    else:
        return False
