from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        sum = [0] * len(s)
        l_candles = [0] * len(s)
        r_candles = [0] * len(s)
        sum[0] = 1 if s[0] == '*' else 0
        l_candles[0] = 0 if s[0] == '*' else 1
        r_candles[-1] = len(s) - 1 if s[-1] == '|' else 0
        # first we calculate the left prefix sum
        for i, a in enumerate(s):
            if i == 0:
                continue
            else:
                sum[i] = sum[i - 1] + 1 if s[i] == '*' else sum[i-1]
                l_candles[i] = i if s[i] == '|' else l_candles[i-1]
        for i in range(len(s)-1, -1, -1):
            # print(a)
            if i == len(s) - 1:
                continue
            else:
                r_candles[i] = i  \
                    if s[i] == '|' else r_candles[i + 1]

        # print(sum)
        # print(l_candles)
        # print(r_candles)
        output = []
        for i in queries:
            first = sum[r_candles[i[0]]]
            second = sum[l_candles[i[1]]]
            # print(first, second, r_candles[i[0]], l_candles[i[1]])
            res = 0 if first > second else second - first
            output.append(res)
        return output


soln = Solution()
print(soln.platesBetweenCandles("***|**|*****|**||**|*",
      [[4, 5], [14, 17]]))

# "***|**|*****|**||**|*"
# "012345678901234567890
