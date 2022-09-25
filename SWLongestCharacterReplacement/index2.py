from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        maxLen = 0
        hashVal = {}
        l, r = 0, 0
        while r < len(s):
            hashVal[s[r]] = hashVal.get(s[r], 0) + 1
            maxF = max(maxF, hashVal[s[r]])
            if len(s[l:r+1]) - maxF <= k:
                maxLen = len(s[l:r+1])
                r += 1

            else:
                hashVal[s[l]] -= 1
                r += 1
                l += 1
        return maxLen


soln = Solution()
print(soln.characterReplacement("AABABBA", 1))
