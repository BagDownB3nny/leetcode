class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        
        start = 0
        end = len(p) - 1
        ans = 0
        
        while start < end:
            lightest = p[start]
            ans += 1
            newLimit = limit - lightest
            while p[end] > newLimit:
                end -= 1
                ans += 1
                if start == end:
                    break
            start += 1
            end -= 1
        if start == end:
            ans += 1
        return ans
