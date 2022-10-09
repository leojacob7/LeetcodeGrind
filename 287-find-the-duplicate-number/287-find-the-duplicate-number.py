class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        index = 0
        while True:
            # print(">", i)
            if nums[i] < 0:
                return nums[index] * -1
            else:
                index = i
                nums[i] *= -1
                i = nums[i]