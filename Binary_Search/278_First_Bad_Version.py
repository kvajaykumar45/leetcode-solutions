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
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid  # The first bad version is at mid or before
            else:
                low = mid + 1  # The first bad version is after mid

        return low  # or return high, both are same at this point

        
