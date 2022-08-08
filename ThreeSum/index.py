def threeSum(nums):
    output = []
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        while l < r:
            start = nums[l]
            end = nums[r]
            threeSum = start + end + nums[i]
            if nums[i] + start + end == 0:
                output.append([nums[i], start, end])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif threeSum > 0:
                r -= 1
            else:
                l += 1
    return output


#        [-4. -1. -1, 0, 1, 2]
a = threeSum([-1, 0, 1, 0])
print(a)
