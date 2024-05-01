class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        toReverse = []
        for i, char in enumerate(word):
            toReverse.append(char)
            if char == ch:
                reverse = "".join(reversed(toReverse))
                return reverse + word[i + 1:]
        return word
