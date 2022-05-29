class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
        if max_sum == 0:
            return max(nums)
        return max_sum
