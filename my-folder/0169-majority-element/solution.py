class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counted = {}
        threshold = len(nums) / 2
        for num in nums:
            if num in counted.keys():
                counted[num] = counted[num] + 1
                if counted[num] > threshold:
                    return num
            else:
                counted[num] = 1
                if counted[num] > threshold:
                    return num

