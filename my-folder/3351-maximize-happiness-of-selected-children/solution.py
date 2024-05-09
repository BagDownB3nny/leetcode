class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h = sorted(happiness, reverse = True)
        ans = 0
        sub = 0
        ptr = 0
        while ptr < k and ptr < len(h):
            if h[ptr] - sub <= 0:
                break
            ans += h[ptr] - sub
            ptr += 1
            sub += 1
            
        return ans
