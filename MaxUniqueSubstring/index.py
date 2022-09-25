def lengthOfLongestSubstring(s):
    hashVal = {}
    curMax = 0
    maxLength = 1
    window = []
    if len(s) == 0:
        return 0
    for i, a in enumerate(s):
        print(a, hashVal, maxLength)
        if (a not in hashVal):
            window.append(a)
            hashVal[a] = 1
            curMax = len(window)
        else:
            tempLen = maxLength
            while a in hashVal and hashVal[a] != 0:
                # print(">>", hashVal, window)
                poppedElem = window.pop(0)
                hashVal[poppedElem] -= 1
                tempLen -= 1
            window.append(a)
            curMax = len(window)
            hashVal[a] += 1
            print(">>", window)

        maxLength = max(curMax, maxLength)
    print(window)
    return maxLength


print(lengthOfLongestSubstring("pwwkew"))
