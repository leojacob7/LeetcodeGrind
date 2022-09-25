from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        print("m", m, " n ", n)
        last_index = 0
        start_index = 0
        end_index = 0
        iteration = 0
        for i in range(0, m*n, m):
            if matrix[i//n][0] < target:
                last_index = i//n
                continue
            else:
                print("i", i//n, matrix[i//n][0], last_index)
                start_index = i//n
                iteration = i

        for i in range(last_index, m*n, m):
            print("here", i)
            if matrix[i//n][0] > target:
                continue
            else:
                print("j", i, i//n, matrix[i//n][0])
                end_index = i//n
        print("start", start_index, "end", end_index)
        return False


solution = Solution()
print(solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16))
