class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        seenBitmaps = [1] + [0] * 1023
        ans = 0
        bitmap = 0
        for c in word:
            bitmap ^= 1 << (ord(c) - ord("a"))
            ans += seenBitmaps[bitmap]
            seenBitmaps[bitmap] += 1
            for n in range(10):
                m = bitmap ^ 1 << n
                ans += seenBitmaps[m]
        return ans
            
