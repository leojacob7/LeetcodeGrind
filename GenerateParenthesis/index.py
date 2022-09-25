from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursiveGenerate(ans, n, openCount, closedCount, str):
            # base case i.e if str length == 2* n i.e balanced parenthesis
            if len(str) == 2 * n:
                ans.append(str)
                return
            if openCount < n:
                recursiveGenerate(ans, n, openCount+1, closedCount, str+"(")
            if closedCount < openCount:
                recursiveGenerate(ans, n, openCount, closedCount + 1, str+")")
        ans = []
        recursiveGenerate(ans, n, 0, 0, "")

        return ans


soln = Solution()
print(soln.generateParenthesis(2))
