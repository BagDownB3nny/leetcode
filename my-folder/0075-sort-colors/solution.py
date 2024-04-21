class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        balls = [0,0,0]
        
        for ball in nums:
            balls[ball] += 1
            
        current = 0
        for i, ball in enumerate(nums):
            
            while not balls[current]:
                current += 1           
            nums[i] = current
            balls[current] -= 1
        return nums
