class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setElem = set(nums)
        maxLength = 0
        length = 0
        for i, a in enumerate(nums):
            if a-1 not in setElem:
                length = 1
                while a+length in setElem:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength