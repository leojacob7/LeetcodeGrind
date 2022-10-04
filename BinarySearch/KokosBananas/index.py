from time import time
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingTime(rate) -> int:
            timeSpent = 0
            for i in piles:
                timeSpent += math.ceil(i/rate)

            return timeSpent

        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            pivot = (l+r)//2
            eatingRate = eatingTime(pivot)
            print(pivot, eatingRate)
            if eatingRate <= h:
                ans = pivot
                r = pivot - 1
            else:
                l = pivot + 1
        return ans


soln = Solution()
print(soln.minEatingSpeed([312884470], 312884469))
