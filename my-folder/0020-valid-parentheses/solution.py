class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                prev_char = stack.pop()
                if open_brackets.index(prev_char) != close_brackets.index(char):
                    return False
        return len(stack) == 0
