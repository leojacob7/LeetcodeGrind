def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l < r:
        area = (r - (l)) * (min(height[l], height[r]))
        print(area, r, l+1, min(height[l], height[r]))
        maxArea = max(area, maxArea)
        if height[l] < height[l+1]:
            l += 1
        else:
            r -= 1
        # code
    print(maxArea)


maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
