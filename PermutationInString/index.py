from typing import List


class Solution:
    def createHash(self, string: str) -> hash:
        hashVal = {}
        for i in string:
            hashVal[i] = hashVal.get(i, 0) + 1
        return hashVal

    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashS1 = {}
        hashS2 = {}
        for i in s1:
            hashS1[i] = hashS1.get(i, 0) + 1

        l = 0
        windowSize = len(s1)
        comparingHash = {}
        while l < len(s2) and l+windowSize <= len(s2):
            if s2[l] not in s1:
                l += 1
            else:
                comparingHash = self.createHash(s2[l:l+windowSize])
                print(comparingHash)
                if comparingHash == hashS1:
                    return True
                else:

                    l += 1
        return False


soln = Solution()

print(soln.checkInclusion("adc", "dcda"))
