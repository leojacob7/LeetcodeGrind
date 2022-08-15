class Solution:
    def checkHashes(self, hash1, hash2):
        for i in hash2.keys():
            if i in hash2 and hash2[i] <= 0:
                continue
            if i not in hash1 or hash1[i] != hash2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        hashVal1 = {}
        hashVal2 = {}
        flag = False
        for i in s1:
            hashVal1[i] = 1 + hashVal1.get(i, 0)
        windowSize = len(s1)
        for i, a in enumerate(s2[:windowSize]):
            hashVal2[a] = 1 + hashVal2.get(a, 0)
        r = windowSize-1
        l = 0
        while r <= len(s2):
            print(l, r, len(s2),  s2[r], hashVal1, hashVal2)
            if self.checkHashes(hashVal1, hashVal2):
                return True
            elif r == len(s2)-1:
                return False
            else:
                hashVal2[s2[l]] -= 1
                l += 1
                r += 1
                hashVal2[s2[r]] = 1 + \
                    hashVal2.get(s2[r], 0)
        return False


soln = Solution()
print(soln.checkInclusion("ab", "qw"))
