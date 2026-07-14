class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        List=[]
        for i in nums:
            s=s+i
            List.append(s)

        return List
        
