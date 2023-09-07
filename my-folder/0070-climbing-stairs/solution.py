class Solution(object):

    def __init__(self):
        self.answers = {}

    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n in self.answers.keys():
            return self.answers[n]
        answer = self.climbStairs(n - 1) + self.climbStairs(n-2)
        self.answers[n] = answer
        return answer

        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n-2)
