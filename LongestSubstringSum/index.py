# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def max_subArray(self, nums) -> int:
    max_sum = -ie4
    cur_sum = nums[0]
    for i in nums:
        cur_sum += i

        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return max_sum