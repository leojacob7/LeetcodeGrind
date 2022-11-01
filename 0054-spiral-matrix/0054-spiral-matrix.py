class Solution:
        def spiralOrder(self, L: List[List[int]]) -> List[int]:
            m = len(L)
            n = len(L[0])
            up, down, left, right = "up", "down", "left", "right"
            direction = right
            res = []
            index = 0
            i, j = 0, 0
            while index < m*n + 30:
                if direction == right:
                    if (j < n and L[i][j] != 'visited'):
                        res.append(L[i][j])
                        L[i][j] = "visited"
                        j += 1
                    else:
                        direction = down
                        j -= 1
                        i += 1
                # direction down
                if direction == down:
                    if (i < m and L[i][j] != 'visited'):
                        res.append(L[i][j])
                        L[i][j] = "visited"
                        i += 1
                    else:
                        direction = left
                        j -= 1
                        i -= 1
                # direction left
                if direction == left:
                    if (j >= 0 and L[i][j] != 'visited'):
                        res.append(L[i][j])
                        L[i][j] = "visited"
                        j -= 1
                    else:
                        direction = up
                        i -= 1
                        j += 1
                        # j = 0
                # direction up
                if direction == up:
                    if (i >= 0 and L[i][j] != "visited"):
                        res.append(L[i][j])
                        L[i][j] = "visited"
                        i -= 1
                    else:
                        direction = right
                        i += 1
                        j += 1

                index += 1

            return res
        