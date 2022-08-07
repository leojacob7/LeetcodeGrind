def maxProfit(prices):
    res = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res


output = maxProfit([7, 2, 8, 1, 6, 4, 1, 2])
print(">>", output)
