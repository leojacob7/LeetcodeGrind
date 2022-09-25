from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            print(area, min(height[l], height[r]), l, r)
            maxArea = max(maxArea, area)
            if height[l] < height[l+1]:
                l += 1
            else:
                r -= 1
        return maxArea


soln = Solution()
print(soln.maxArea([1, 1]))
