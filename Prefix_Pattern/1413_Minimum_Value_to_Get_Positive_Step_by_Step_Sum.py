class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=0
        start=1
        for i in nums:
            prefix+=i
            start=max(start,1-prefix)
        return start
