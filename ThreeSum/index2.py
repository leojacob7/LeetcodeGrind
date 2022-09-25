from typing import List


class Solution:
    def twoSum(self, nums: List[int], target, elem):
        l = 0
        r = len(nums) - 1
        res = []
        print(">>", nums, elem)
        while l < r:
            threeSum = nums[l] + nums[r] + elem
            if threeSum == 0:
                # print("ere", res, nums[l], nums[r], nums)
                res.append([elem, nums[l], nums[r]])
                l += 1
                # print("res", res)
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif threeSum < 0:
                l += 1
            else:
                r -= 1
        # print("res return", res)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = sorted(nums)
        print(sortedList)
        # print(sortedList)
        i = 0
        res = []
        for i, a in enumerate(sortedList):
            # print(i, a)
            firstNum = a
            l = i
            if i != 0 and a == sortedList[i-1]:
                continue
            output = self.twoSum(sortedList[l+1:], -firstNum, firstNum)
            # print("output", output)
            if len(output) == 0:
                continue
            else:
                for i in output:
                    res.append(i)
                # print("output1", res)
            # print(elem)
            # res.append(elem)

        if len(res) == 0:
            return []
        return res


soln = Solution()
print(soln.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
