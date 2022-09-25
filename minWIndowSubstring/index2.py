class Solution:
    def minWindow(self, s: str, t: str) -> str:
        print("here")
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        lastOccur = 0
        minLength = 10000
        hashValT = {}
        for i in t:
            hashValT[i] = 1 + hashValT.get(i, 0)
        hashValS = {}
        required = 0
        tempRequired = required
        for i in hashValT.keys():
            required += hashValT[i]
        while l < len(s):
            if s[r] not in hashValT:
                r += 1
            else:
                hashValS[s[r]] = 1 + hashValS.get(s[r], 0)
                if hashValS[s[r]] >= hashValT[s[r]]:
                    tempRequired -= 1

        return minLength


soln = Solution()
print(soln.minWindow("ADOBECODEBANC", "ABC"))
# print(soln.minWindow("0123456789", "ABC"))

# A D O B E C O D E B A N C
# 0 1 2 3 4 5 6 7 8 9 10 11 12
