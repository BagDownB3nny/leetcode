class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        ans = -1
        for n in nums:
            if n * -1 in s:
                ans = max(abs(n), ans)
            if n not in s:
                s.add(n)
        return ans
        
