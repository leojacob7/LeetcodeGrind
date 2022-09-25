from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        r = len(temperatures) - 1
        stack = []
        for r, a in reversed(list(enumerate(temperatures))):
            if r == len(temperatures) - 1:
                stack.append(r)
                output[r] = 0
            else:
                if temperatures[stack[-1]] > temperatures[r]:
                    output[r] = stack[-1]-r
                    stack.append(r)
                else:
                    while stack and temperatures[stack[-1]] <= temperatures[r]:
                        stack.pop()
                    if len(stack) == 0:
                        output[r] = 0
                        stack.append(r)
                    else:
                        output[r] = stack[-1]-r
                        stack.append((r))

            # r -= 1
        return output


soln = Solution()
print(soln.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
