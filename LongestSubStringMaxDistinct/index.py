from typing import List


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k <= 0:
            return 0
        if len(s) < k:
            return len(s)
        maxLength = 0
        hashVal = {}
        l, r = 0, 0
        while r < len(s):
            hashVal[s[r]] = hashVal.get(s[r], 0) + 1
            print(hashVal, s[l])
            if len(hashVal.keys()) >= k + 1:
                hashVal[s[l]] -= 1
                if hashVal[s[l]] == 0:
                    del hashVal[s[l]]
                l += 1
                r += 1
            else:
                r += 1
            print(s[l:r], hashVal)
            maxLength = max(maxLength, len(s[l:r]))

        return maxLength


soln = Solution()
print(soln.lengthOfLongestSubstringKDistinct('eceba', 2))
