class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [int(i) for each in nums for i in str(each)]
        return result
        
