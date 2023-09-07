class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        largest_sum = -999999
        for num in nums:
            current_sum += num
            if current_sum > largest_sum:
                largest_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return largest_sum
