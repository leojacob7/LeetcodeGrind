class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashVal1 = {}
        hashVal2 = {}
        for i in nums:
            hashVal1[i] = 1 + hashVal1.get(i, 0)
        for j in hashVal1.keys():
            key = hashVal1[j]
            hashVal2[key] = [j] + hashVal2.get(key, [])

        res = [-1] * (len(nums)+1)
        for i in hashVal2.keys():
            res[i] = hashVal2[i]
        output = []
        for i in reversed(res):
            if i == -1:
                continue
            k -= len(i)
            for j in i:
                output.append(j)

            if k <= 0:
                break
        return output
            
                            