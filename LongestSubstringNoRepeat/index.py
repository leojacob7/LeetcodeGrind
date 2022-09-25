class Solution:
    def lengthOfLongestSubstring(self, stringVal: str) -> int:
        hashVal = {}
        leng = 0
        l, r = 0, 0

        while r < len(stringVal):
            if stringVal[r] in hashVal and hashVal[stringVal[r]] > 0:
                hashVal[stringVal[l]] -= 1
                l += 1
                # r += 1
            else:
                hashVal[stringVal[r]] = 1
                print(r, l)
                leng = max(leng, r-l+1)
                r += 1
        return leng


soln = Solution()
print(soln.lengthOfLongestSubstring("aaa"))
