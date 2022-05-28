class Solution(object):
    def isValid(self, s):
        stack = []
        for bracket in s:
            print(bracket)
            if bracket == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False
            elif bracket == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != '[':
                    return False
            elif bracket == '}':
                if len(stack) == 0:
                    return False
                if stack.pop() != '{':
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0
