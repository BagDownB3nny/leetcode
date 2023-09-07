class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set()
        length = 0
        for letter in s:
            if letter not in letters:
                letters.add(letter)
            else:
                letters.remove(letter)
                length += 2
        if len(letters) > 0:
            return length + 1
        return length
