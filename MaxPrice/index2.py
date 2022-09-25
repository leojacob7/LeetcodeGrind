from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxVal = 0
        lLow = l
        rLow = r
        while r < len(prices):
            maxVal = max(prices[r]-prices[l], maxVal)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        return maxVal


soln = Solution()
print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
