from typing import List


class Solution:
    def getBound(self, nums: int, target: int, isFirstBound, pivot=0) -> int:
        bound = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = l + ((r - l) // 2)
            # if isFirstBound:
            # print(pivot, r, l)
            if nums[pivot] == target:
                if isFirstBound:
                    # print(nums[pivot-1], pivot, nums[pivot-1] < target)
                    if nums[pivot-1] < target:
                        return pivot
                    else:
                        r = pivot - 1
                else:
                    if nums[pivot+1] > target:
                        return pivot
                    else:
                        l = pivot + 1
            if nums[pivot] < target:
                l = pivot+1
            else:
                r = pivot - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        firstBound = self.getBound(nums, target, True)
        secondBound = self.getBound(nums, target, False)
        if firstBound == -1 and secondBound == -1:
            return [-1, -1]
        else:
            return [firstBound, secondBound]


soln = Solution()
print(soln.searchRange([7, 7, 7, 8, 8, 10], 6))
