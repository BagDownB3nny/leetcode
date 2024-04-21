class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = []
        upper = []
        special = []
        for c in word:
            if c.lower() in special:
                continue
            if c.lower() == c:
                lower.append(c)
                if c.upper() in upper:
                    special.append(c.lower())
            if c.upper() == c:
                upper.append(c)
                if c.lower() in lower:
                    special.append(c.lower())
        return len(special)
