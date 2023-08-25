class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_nums.keys():
                first_index = seen_nums[diff]
                second_index = i
                return [ first_index, second_index ]
            else:
                seen_nums[num] = i
