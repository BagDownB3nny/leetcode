class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            start_char = s[start]
            end_char = s[end]
            if not start_char.isalnum():
                start += 1
                continue
            if not end_char.isalnum():
                end -= 1
                continue
            if start_char.lower() != end_char.lower():
                return False
            start += 1
            end -= 1
        return True
