# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # first bad version is always between start and end
        start = 1
        end = n
        while start < end:
            middle = start + (end - start) / 2
            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1
        return end
