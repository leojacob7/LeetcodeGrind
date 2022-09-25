class Solution:
    def topKFrequent(self, nums, k):
        hashVal = {}
        countSortHash = {}
        for i in nums:
            hashVal[i] = 1 + hashVal.get(i, 0)
        print(hashVal)
        for i in hashVal.keys():
            if hashVal[i] in countSortHash:
                curContent = countSortHash[hashVal[i]]
                curContent.append(i)

                countSortHash[hashVal[i]] = curContent
            else:
                countSortHash[hashVal[i]] = [i]
        res = []
        print(countSortHash, (sorted(countSortHash.keys())))
        for i in reversed(sorted(countSortHash.keys())):
            if len(countSortHash[i]) == 0:
                continue
            else:
                k -= len(countSortHash[i])
                for j in countSortHash[i]:
                    res.append(j)
                # res.append(countSortHash[i])
                if k <= 0:
                    return res


soln = Solution()
print("output", soln.topKFrequent([1, 1, 1, 2, 2, 3], 2))
