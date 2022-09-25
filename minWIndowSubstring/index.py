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
        temp = 0
        while r < len(s):
            print("printing", s[r], hashValT, hashValS, r, l, lastOccur)
            if s[r] in hashValT:
                hashValS[s[r]] = 1 + hashValS.get(s[r], 0)
                print("hashValS", hashValS)
                if(hashValS == hashValT):
                    minLength = min(minLength, (r-l)+1)
                    print("minLength", minLength, r, l, lastOccur)
                    # r = (r - l) + 1
                    # r = lastOccur + len(t) - 1
                    r = lastOccur+1
                    l = lastOccur
                    hashValS = {s[l]: 1}
                else:
                    lastOccur = r
                    r += 1
            else:
                r += 1
        print(">>", minLength)
        return minLength


soln = Solution()
print(soln.minWindow("ADOBECODEBANC", "ABC"))
# print(soln.minWindow("0123456789", "ABC"))

# A D O B E C O D E B A N C
# 0 1 2 3 4 5 6 7 8 9 10 11 12
