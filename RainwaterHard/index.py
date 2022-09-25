from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 1
        maxLeft = []
        maxRight = [0]*(len(height)-1)
        maxVal = height[0]
        for i, a in enumerate(height):
            if i == 0:
                maxLeft.append(0)
                maxVal = 0
            else:
                maxLeft.append(maxVal)
                maxVal = max(maxVal, a)

        maxVal = height[-1]
        for i, a in reversed(list(enumerate(height))):
            if i == len(maxLeft)-1:
                maxRight.append(0)
            else:
                maxRight[i] = maxVal
                maxVal = max(maxVal, a)
        # maxRight = reversed(maxRight)
        print(maxLeft)
        print(maxRight)
        sumArr = [0]*(len(height))
        for i in range(len(height)):
            val = min(maxLeft[i], maxRight[i])
            sumArr[i] = max(0, val - height[i])

        print(sum(sumArr))
        return ans


soln = Solution()
print(soln.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
