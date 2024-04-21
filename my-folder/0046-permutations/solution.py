class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if len(nums) == 1:
                return [nums]
            ans = []
            for i, num in enumerate(nums):
                newNums = nums.copy()
                newNums.pop(i)
                perms = helper(newNums)
                for perm in perms:
                    perm.append(num)
                ans = ans + perms
            return ans
        
        return helper(nums)
        
