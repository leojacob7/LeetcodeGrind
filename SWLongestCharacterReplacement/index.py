def characterReplacement(s, k):
    maxF = 0
    l = 0
    hashVal = {}
    maxLength = 0
    if len(s) == 0:
        return 1
    for r, a in enumerate(s):
        curMax = r-l
        hashVal[a] = hashVal[a] + 1 if a in hashVal else 1
        maxF = max(maxF, hashVal[a])
        if maxF > curMax:
            l += 1
        maxLength = max(curMax, maxLength)
    return maxLength


print(characterReplacement("ABBA", 2))
