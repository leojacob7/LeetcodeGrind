from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # create a dequeue which has a strict decreasing array
        deq = deque()
        l = r = 0
        print("Here")
        while r < len(nums):
            print(r, deq)
            if deq and r-k == deq[0]:
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[r]:
                deq.pop()
            deq.append(r)
            if r >= k-1:
                output.append(nums[deq[0]])
            r += 1
        print(output)
        return output


soln = Solution()
print("here")
print(soln.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
