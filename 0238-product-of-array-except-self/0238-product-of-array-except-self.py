class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            prefix = postFix = 1
            res = [1] * (len(nums))
            for i, a in enumerate(nums):
                res[i] *= prefix
                prefix *= a

            for j in range(len(nums) - 1, -1, -1):
                res[j] *= postFix
                postFix *= nums[j]
            return res